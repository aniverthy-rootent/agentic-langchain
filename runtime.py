"""LangChain runtime: each agent is a prompt | model | parser chain (LCEL).

A "layer" of agents runs concurrently via RunnablePassthrough.assign, and the
layers are composed with the | operator.
"""
from __future__ import annotations

from typing import Any, List, Optional

from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models.chat_models import SimpleChatModel
from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

from common.flow import compose_input, dependencies, execution_layers, system_prompt
from common.offline_llm import offline_complete


class OfflineChatModel(SimpleChatModel):
    """A LangChain chat model with no network access. Swap for ChatOpenAI etc."""

    @property
    def _llm_type(self) -> str:
        return "offline"

    def _call(self, messages: List[BaseMessage], stop: Optional[List[str]] = None,
              run_manager: Optional[CallbackManagerForLLMRun] = None, **kwargs: Any) -> str:
        system = next((m.content for m in messages if m.type == "system"), "")
        user = next((m.content for m in reversed(messages) if m.type == "human"), "")
        return offline_complete(str(system), str(user))


PROMPT = ChatPromptTemplate.from_messages([("system", "{system}"), ("human", "{user}")])


def build_chain(agents, task, pattern, model=None):
    model = model or OfflineChatModel()
    deps = dependencies(pattern, len(agents))

    def agent_chain(i):
        key, role, instr = agents[i]

        def prepare(state: dict) -> dict:
            ups = [(agents[j][1], state[agents[j][0]]) for j in deps[i]]
            return {"system": system_prompt(role, instr), "user": compose_input(task, ups)}

        return RunnableLambda(prepare) | PROMPT | model | StrOutputParser()

    chain = RunnableLambda(lambda x: {})
    for layer in execution_layers(pattern, len(agents)):
        chain = chain | RunnablePassthrough.assign(**{agents[i][0]: agent_chain(i) for i in layer})
    return chain


def run_app(title, agents, task, pattern="sequential", provider=None) -> dict:
    state = build_chain(agents, task, pattern).invoke({})
    return {key: state[key] for key, _, _ in agents}
