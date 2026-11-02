"""Interview Preparation Coach

Task: Prepare for a staff-engineer system design interview.
Framework: LangChain (LCEL)
"""
from runtime import run_app

SLUG = 'interview_prep'
TITLE = 'Interview Preparation Coach'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Prepare for a staff-engineer system design interview.'

# (key, role, instruction)
AGENTS = [
    ('role_researcher', 'Role Researcher', 'Describe the role expectations.'),
    ('question_generator', 'Question Generator', 'Generate questions.'),
    ('mock_interviewer', 'Mock Interviewer', 'Run a mock Q&A.'),
    ('answer_evaluator', 'Answer Evaluator', 'Score answers.'),
    ('study_planner', 'Study Planner', 'Build a 2-week plan.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
