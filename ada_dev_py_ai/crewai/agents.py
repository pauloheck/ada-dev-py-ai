from crewai import Agent


def agent_po(input: str):
    return Agent(
        role='produt owner',
        goal='Criar uma historia para desenvolvimento com os seguintes dados ' + input,
        backstory="""
            Como especialista em desenvolvimento de software
            Você tem profundo conhecimento em metodologias ágeis e vasta experiência no mapeamento de requisitos""",
        verbose=True,
    )
