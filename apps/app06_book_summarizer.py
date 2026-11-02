"""Long-Document Summarizer

Task: Summarize a 300-page market research report.
Framework: LangChain (LCEL)
"""
from runtime import run_app

SLUG = 'book_summarizer'
TITLE = 'Long-Document Summarizer'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Summarize a 300-page market research report.'

# (key, role, instruction)
AGENTS = [
    ('chunker', 'Chunker', 'Split into sections.'),
    ('section_summarizer', 'Section Summarizer', 'Summarize each section.'),
    ('theme_finder', 'Theme Finder', 'Find cross-cutting themes.'),
    ('contradiction_checker', 'Contradiction Checker', 'Spot inconsistencies.'),
    ('executive_summarizer', 'Executive Summarizer', 'Write a one-page brief.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
