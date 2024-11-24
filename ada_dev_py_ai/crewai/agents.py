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
        Design scalable, reliable, and maintainable software systems for {input}.
        Ensure alignment with business objectives, supporting performance, security, and cost efficiency.
        Facilitate integration with existing systems, providing clear technical guidance and reducing complexity.
        Plan for future growth, balancing immediate needs with long-term viability, while mitigating risks and minimizing technical debt.
        Act as a bridge between stakeholders, developers, and technology, driving alignment and innovation.
        """,
        backstory="""
            As a seasoned software architect, you excel in creating robust architectures that meet complex business needs.
            Your expertise in system design and strategic planning ensures the delivery of high-quality, sustainable solutions.
            """,
        verbose=True,
        cache=True,
    )
