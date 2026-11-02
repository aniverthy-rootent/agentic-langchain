"""Natural-language to SQL Copilot

Task: Answer: which 5 products had the highest return rate last quarter?
Framework: LangChain (LCEL)
"""
from runtime import run_app

SLUG = 'sql_copilot'
TITLE = 'Natural-language to SQL Copilot'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Answer: which 5 products had the highest return rate last quarter?'

# (key, role, instruction)
AGENTS = [
    ('schema_reader', 'Schema Reader', 'Summarize tables.'),
    ('question_interpreter', 'Question Interpreter', 'Restate the question precisely.'),
    ('sql_writer', 'SQL Writer', 'Write the query.'),
    ('query_validator', 'Query Validator', 'Check safety and syntax.'),
    ('result_explainer', 'Result Explainer', 'Explain results in plain English.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
