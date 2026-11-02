"""Resume Tailor

Task: Tailor a resume to a product manager job posting.
Framework: LangChain (LCEL)
"""
from runtime import run_app

SLUG = 'resume_tailor'
TITLE = 'Resume Tailor'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Tailor a resume to a product manager job posting.'

# (key, role, instruction)
AGENTS = [
    ('job_parser', 'Job Parser', 'Extract requirements.'),
    ('experience_mapper', 'Experience Mapper', 'Map experience to requirements.'),
    ('bullet_rewriter', 'Bullet Rewriter', 'Rewrite bullets with metrics.'),
    ('ats_optimizer', 'ATS Optimizer', 'Add keywords.'),
    ('proofreader', 'Proofreader', 'Fix grammar and consistency.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
