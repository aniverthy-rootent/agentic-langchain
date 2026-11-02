"""Patent Landscape Scanner

Task: Scan prior art for a foldable solar charger.
Framework: LangChain (LCEL)
"""
from runtime import run_app

SLUG = 'patent_search'
TITLE = 'Patent Landscape Scanner'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Scan prior art for a foldable solar charger.'

# (key, role, instruction)
AGENTS = [
    ('claim_parser', 'Claim Parser', 'Break the idea into claims.'),
    ('query_builder', 'Query Builder', 'Build search queries.'),
    ('prior_art_reviewer', 'Prior Art Reviewer', 'Assess candidate patents.'),
    ('novelty_assessor', 'Novelty Assessor', 'Estimate novelty.'),
    ('landscape_reporter', 'Landscape Reporter', 'Write the landscape summary.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
