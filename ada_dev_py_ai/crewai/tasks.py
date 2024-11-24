from crewai import Task

from ada_dev_py_ai.crewai.agents import agent_po, agent_test
from ada_dev_py_ai.models import StoryModel, TestModel


def task_create_story(input: str):
    return Task(
        description='Create a development story with the following data ' + input,
        expected_output="""
        a software development story with the provided data
        the output should be a text with the software development story
        """,
        output_json=StoryModel,
        agent=agent_po(input),
    )


def task_create_test(input: str):
    return Task(
        description='Create comprehensive test cases for the following requirements ' + input,
        expected_output="""
        a list of detailed test cases covering all critical scenarios
        the output should be a set of test cases ensuring software quality
        """,
        output_json=TestModel,
        agent=agent_test(input),
    )
