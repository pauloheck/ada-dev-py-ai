import logging
from crewai import Crew

# Configuração básica do logging
logging.basicConfig(level=logging.DEBUG)

from ada_dev_py_ai.crewai.agents import agent_po, agent_test
from ada_dev_py_ai.crewai.tasks import task_create_story, task_create_test


def create_test_ai(input: str):
    logging.debug(f"Creating test AI with input: {input}")
    crew = Crew(agents=[agent_test(input)], tasks=[task_create_test(input)], memory=True, verbose=True)

    result = crew.kickoff()
    print(result.json_dict)

    return {'status': 'success', 'data': result.json_dict}


def create_story_ai(input: str):
    logging.debug(f"Creating story AI with input: {input}")
    crew = Crew(agents=[agent_po(input)], tasks=[task_create_story(input)], memory=True, verbose=True)

    result = crew.kickoff()
    print(result.json_dict)

    return {'status': 'success', 'data': result.json_dict}
