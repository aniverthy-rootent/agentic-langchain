"""Technical Documentation Writer

Task: Document a REST API for a payments service.
Framework: LangChain (LCEL)
"""
from runtime import run_app

SLUG = 'technical_docs'
TITLE = 'Technical Documentation Writer'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Document a REST API for a payments service.'

# (key, role, instruction)
AGENTS = [
    ('endpoint_cataloger', 'Endpoint Cataloger', 'List endpoints.'),
    ('example_generator', 'Example Generator', 'Write request/response samples.'),
    ('concept_explainer', 'Concept Explainer', 'Write conceptual guides.'),
    ('error_documenter', 'Error Documenter', 'Document error codes.'),
    ('docs_reviewer', 'Docs Reviewer', 'Check consistency.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
