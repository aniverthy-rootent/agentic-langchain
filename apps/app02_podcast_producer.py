"""Podcast Show-notes Producer

Task: Create show notes for a 50-minute interview on remote work.
Framework: LangChain (LCEL)
"""
from runtime import run_app

SLUG = 'podcast_producer'
TITLE = 'Podcast Show-notes Producer'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Create show notes for a 50-minute interview on remote work.'

# (key, role, instruction)
AGENTS = [
    ('transcript_segmenter', 'Transcript Segmenter', 'Split by topic.'),
    ('chapter_namer', 'Chapter Namer', 'Name chapters.'),
    ('quote_picker', 'Quote Picker', 'Select memorable quotes.'),
    ('show_notes_writer', 'Show Notes Writer', 'Write the notes.'),
    ('social_clipper', 'Social Clipper', 'Propose social posts.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
