from crewai import Task

from ada_dev_py_ai.crewai.agents import agent_po


def task_create_story(input: str):
    return Task(
        description='Criar uma história para desenvolvimento com os seguintes dados ' + input,
        expected_output='uma história de desenvolvimento de software com os dados fornecidos',
        output_json=True,
        output_pydantic=True,
        agent=agent_po(),
    )
