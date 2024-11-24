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

def agent_software_architect(input: str):
    return Agent(
        role='software architect',
        goal=f"""
        Design and implement cutting-edge software architectures for {input}.
        Ensure systems are scalable, secure, and maintainable, aligning with business goals.
        Innovate by integrating the latest technologies and methodologies.
        Provide strategic guidance to development teams, ensuring best practices and architectural integrity.
        """,
        backstory="""
            As a highly intelligent software architect, you possess a deep understanding of modern software design principles.
            Your expertise spans across various domains, allowing you to craft architectures that are both innovative and practical.
            You are adept at balancing technical excellence with business needs, ensuring long-term success and sustainability.
            """,
        verbose=True,
        cache=True,
    )
