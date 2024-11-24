from crewai import Agent


def agent_po(input: str):
    return Agent(
        role='product owner',
        goal='Create a development story with the following data ' + input,
        backstory="""
            As a software development specialist,
            you have deep knowledge in agile methodologies and extensive experience in requirements mapping.""",
        verbose=True,
        cache=True,
    )


def agent_test(input: str):
    return Agent(
        role='test engineer',
        goal='Create comprehensive test cases for the provided requirements: ' + input,
        backstory="""
            As an experienced test engineer,
            you specialize in ensuring software quality through rigorous and detailed testing.
            You have a deep understanding of testing methodologies and can identify critical test scenarios.""",
        verbose=True,
        cache=True,
    )

