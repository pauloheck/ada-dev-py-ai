from crewai import Task

from ada_dev_py_ai.crewai.agents import agent_po, agent_test
from ada_dev_py_ai.models import StoryModel


def task_create_story(input: str):
    return Task(
        description='Criar uma história para desenvolvimento com os seguintes dados ' + input,
        expected_output="""
        uma história de desenvolvimento de software com os dados fornecidos
        a Saida deve ser um texto com a história de desenvolvimento de software
        """,
        output_json=StoryModel,
        agent=agent_po(input),
    )


def task_create_test(input: str):
    return Task(
        description='Criar casos de teste abrangentes para os seguintes requisitos ' + input,
        expected_output="""
        uma lista de casos de teste detalhados que cobrem todos os cenários críticos
        a saída deve ser um conjunto de casos de teste que garantam a qualidade do software
        """,
        output_json=None,  # Substitua por um modelo apropriado se necessário
        agent=agent_test(input),
    )
