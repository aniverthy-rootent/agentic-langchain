# agentic-langchain

**11 multi-agent applications built with LangChain (LCEL).**  
Theme: _Knowledge, content & language workflows as LCEL chains_

[LangChain](https://python.langchain.com) composes LLM steps with the LangChain Expression Language (LCEL): small `Runnable`s joined with `|`.

## Quick start (no API key needed)

```bash
pip install -r requirements.txt
python run_all.py                       # run all 11 apps
python -m apps.app01_newsletter_curator   # run a single app
pytest -q                               # smoke tests for every app
```

Every app runs against a deterministic offline model (`common/offline_llm.py`) so you can watch the orchestration work without credentials.

## How it works

Each agent is `prepare | ChatPromptTemplate | chat model | StrOutputParser`. Agents in the same layer run in parallel through `RunnablePassthrough.assign`; layers are chained with `|`.

## Using a real model

Pass a real chat model to `build_chain(..., model=ChatOpenAI(...))` (or `ChatAnthropic`, `ChatGoogleGenerativeAI`, `ChatOllama`) after installing the matching `langchain-*` provider package and setting its API key.

## Applications

| # | Application | Agents | Roles |
|---|---|---|---|
| 1 | Newsletter Curator | 5 | Topic Scout, Article Summarizer, Quality Filter, Headline Writer, Layout Editor |
| 2 | Podcast Show-notes Producer | 5 | Transcript Segmenter, Chapter Namer, Quote Picker, Show Notes Writer, Social Clipper |
| 3 | Translation & Localization | 5 | Source Analyzer, Translator, Cultural Adapter, Terminology Checker, Back-Translator |
| 4 | Resume Tailor | 5 | Job Parser, Experience Mapper, Bullet Rewriter, ATS Optimizer, Proofreader |
| 5 | Technical Documentation Writer | 5 | Endpoint Cataloger, Example Generator, Concept Explainer, Error Documenter, Docs Reviewer |
| 6 | Long-Document Summarizer | 5 | Chunker, Section Summarizer, Theme Finder, Contradiction Checker, Executive Summarizer |
| 7 | Email Triage Assistant | 5 | Classifier, Priority Scorer, Reply Drafter, Calendar Matcher, Digest Writer |
| 8 | Natural-language to SQL Copilot | 5 | Schema Reader, Question Interpreter, SQL Writer, Query Validator, Result Explainer |
| 9 | Interview Preparation Coach | 5 | Role Researcher, Question Generator, Mock Interviewer, Answer Evaluator, Study Planner |
| 10 | Speech Writer | 5 | Story Collector, Tone Setter, Draft Writer, Timing Coach, Polisher |
| 11 | Patent Landscape Scanner | 5 | Claim Parser, Query Builder, Prior Art Reviewer, Novelty Assessor, Landscape Reporter |

Full per-agent instructions are in [AGENTS.md](AGENTS.md).

Each app uses one of two data-flow patterns (see `common/flow.py`):
`sequential` (each agent builds on the previous) or `fanout` (a planner, parallel specialists, then a merger).

## License

MIT
