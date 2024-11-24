from crewai import Crew

from ada_dev_py_ai.crewai.agents import agent_po, agent_test
from ada_dev_py_ai.crewai.tasks import task_create_story, task_create_test


def create_test_ai(input: str):
    crew = Crew(agents=[agent_test(input)], tasks=[task_create_test(input)], memory=True, verbose=True)

    result = crew.kickoff()
    print(result.json_dict)

    return {'status': 'success', 'data': result.json_dict}


def create_story_ai(input: str):
    crew = Crew(agents=[agent_po(input)], tasks=[task_create_story(input)], memory=True, verbose=True)

    result = crew.kickoff()
    print(result.json_dict)

    return {'status': 'success', 'data': result.json_dict}
