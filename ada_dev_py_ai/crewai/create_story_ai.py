import json

import importlib_metadata
from crewai import Crew

from ada_dev_py_ai.crewai.agents import agent_po
from ada_dev_py_ai.crewai.tasks import task_create_story


def create_story_ai(input: str) -> str:
    """
    Create a story using the Crew AI framework.

    Args:
        input (str): The input string containing story requirements.

    Returns:
        str: A JSON string representing the created story.
    """
    # Example of handling entry points with the new API
    entry_points = importlib_metadata.entry_points()
    # Use the new API to filter entry points

    my_crew = Crew(
        agents=[agent_po(input)],
        tasks=[task_create_story(input)]
    )

    # Start the crew with the given inputs
    crew = my_crew.kickoff(inputs={'input': input})

    # Return the crew object as a JSON string
    return json.dumps(crew.json_dict())
