from crewai import Crew

from ada_dev_py_ai.crewai.agents import agent_po
from ada_dev_py_ai.crewai.tasks import task_create_story


def create_story_ai(input: str):
    crew = Crew(agents=[agent_po(input)], tasks=[task_create_story(input)]).kickoff()

    # Return the crew object as a JSON string
    return crew
