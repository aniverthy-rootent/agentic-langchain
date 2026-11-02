"""Email Triage Assistant

Task: Triage 50 unread executive emails.
Framework: LangChain (LCEL)
"""
from runtime import run_app

SLUG = 'email_triage'
TITLE = 'Email Triage Assistant'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Triage 50 unread executive emails.'

# (key, role, instruction)
AGENTS = [
    ('classifier', 'Classifier', 'Label each email.'),
    ('priority_scorer', 'Priority Scorer', 'Rank by urgency.'),
    ('reply_drafter', 'Reply Drafter', 'Draft replies.'),
    ('calendar_matcher', 'Calendar Matcher', 'Propose meeting times.'),
    ('digest_writer', 'Digest Writer', 'Produce a morning digest.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
