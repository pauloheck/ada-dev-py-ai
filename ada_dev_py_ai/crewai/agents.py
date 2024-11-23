from crewai import Agent


def agent_po(input: str):
    print('passou aqui no agent_po')
    return Agent(
        role='agent role',
        goal='Criar uma historia para desenvolvimento com os seguintes dados ' + input,
        backstory="""
            Como especialista em desenvolvimento de software
            Você tem profundo conhecimento em metodologias ágeis e vasta experiência no mapeamento de requisitos""",
        verbose=True,
    )
