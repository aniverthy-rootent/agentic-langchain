"""Newsletter Curator

Task: Build this week's AI engineering newsletter.
Framework: LangChain (LCEL)
"""
from runtime import run_app

SLUG = 'newsletter_curator'
TITLE = 'Newsletter Curator'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = "Build this week's AI engineering newsletter."

# (key, role, instruction)
AGENTS = [
    ('topic_scout', 'Topic Scout', 'Pick the top themes.'),
    ('article_summarizer', 'Article Summarizer', 'Summarize candidate articles.'),
    ('quality_filter', 'Quality Filter', 'Drop low-value links.'),
    ('headline_writer', 'Headline Writer', 'Write headlines.'),
    ('layout_editor', 'Layout Editor', 'Assemble the issue.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
