from json import dumps as json

from crewai import Crew

from ada_dev_py_ai.crewai.agents import agent_po
from ada_dev_py_ai.crewai.tasks import task_create_story


def create_story_ai(input: str):
    my_crew = Crew(agents=[agent_po(input)], tasks=[task_create_story(input)])
    crew = my_crew.kickoff(inputs={'input': input})

    # return the crew object as a json object

    return json(crew.json_dict())
