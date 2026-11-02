"""Translation & Localization

Task: Localize a mobile app onboarding flow into Japanese.
Framework: LangChain (LCEL)
"""
from runtime import run_app

SLUG = 'translation_localizer'
TITLE = 'Translation & Localization'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Localize a mobile app onboarding flow into Japanese.'

# (key, role, instruction)
AGENTS = [
    ('source_analyzer', 'Source Analyzer', 'Find idioms and variables.'),
    ('translator', 'Translator', 'Translate the strings.'),
    ('cultural_adapter', 'Cultural Adapter', 'Adapt tone and imagery.'),
    ('terminology_checker', 'Terminology Checker', 'Enforce the glossary.'),
    ('back_translator', 'Back-Translator', 'Verify meaning by back-translation.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
