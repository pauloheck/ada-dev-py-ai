from crewai import Task

from ada_dev_py_ai.crewai.agents import agent_po
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
