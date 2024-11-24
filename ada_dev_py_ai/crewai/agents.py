from crewai import Agent


def agent_po(input: str):
    return Agent(
        role='produt owner',
        goal='Criar uma historia para desenvolvimento com os seguintes dados ' + input,
        backstory="""
            Como especialista em desenvolvimento de software
            Você tem profundo conhecimento em metodologias ágeis e vasta experiência no mapeamento de requisitos""",
        verbose=True,
        cache=True,
    )


def agent_test(input: str):
    return Agent(
        role='test engineer',
        goal='Criar casos de teste abrangentes para os requisitos fornecidos: ' + input,
        backstory="""
            Como engenheiro de teste experiente,
            você é especializado em garantir a qualidade do software através de testes rigorosos e detalhados.
            Você tem um profundo entendimento de metodologias de teste e é capaz de identificar cenários de teste críticos.""",
        verbose=True,
        cache=True,
    )

def agent_software_architect(input: str):
    return Agent(
        role='software architect',
        goal="""
        Create a technology design scalable, reliable, and maintainable software systems,
        for """
        + input
        + """that align with business objectives,
        ensure the architecture supports performance, security,
        and cost efficiency while enabling integration with existing systems,
        the Architects provide clear technical guidance, reduce complexity,
        and plan for future growth and balance immediate needs with long-term viability,
        mitigating risks and minimizing technical debt.
        Ultimately, they act as the bridge between stakeholders, developers, and technology, driving alignment and innovation.
        """,
        backstory="""
            Como especialista em desenvolvimento de software
            Você tem profundo conhecimento em metodologias ágeis e vasta experiência no mapeamento de requisitos""",
        verbose=True,
        cache=True,
    )
