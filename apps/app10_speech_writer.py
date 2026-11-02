"""Speech Writer

Task: Write a 5-minute wedding toast for a best friend.
Framework: LangChain (LCEL)
"""
from runtime import run_app

SLUG = 'speech_writer'
TITLE = 'Speech Writer'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Write a 5-minute wedding toast for a best friend.'

# (key, role, instruction)
AGENTS = [
    ('story_collector', 'Story Collector', 'Gather anecdotes.'),
    ('tone_setter', 'Tone Setter', 'Choose humor level.'),
    ('draft_writer', 'Draft Writer', 'Write the draft.'),
    ('timing_coach', 'Timing Coach', 'Trim to length.'),
    ('polisher', 'Polisher', 'Refine delivery cues.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
