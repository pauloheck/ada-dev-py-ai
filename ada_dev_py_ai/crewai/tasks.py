from crewai import Task

from ada_dev_py_ai.crewai.agents import agent_po, agent_test
from ada_dev_py_ai.models import ListStoryModel, ListTestModel


def task_create_story(input: str):
    return Task(
        description='Create comprehensives List of development story with the following data ' + input,
        expected_output="""
        a software development story with the provided data
        the output should be a text with a List of software development story
        the output language should be in portuguese (pt-br)
        """,
        output_json=ListStoryModel,
        agent=agent_po(input),
    )


def task_create_test(input: str):
    return Task(
        description='Create comprehensives List of test cases for the following story ' + input,
        expected_output="""
        a list of detailed test cases covering all critical scenarios
        the output should be a lista of test cases ensuring software quality
        the output language should be in portuguese (pt-br)
        """,
        output_json=ListTestModel,
        agent=agent_test(input),
    )
