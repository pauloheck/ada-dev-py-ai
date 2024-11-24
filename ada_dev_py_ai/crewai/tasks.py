from crewai import Task

from ada_dev_py_ai.crewai.agents import agent_developer, agent_po, agent_project_manager, agent_software_architect, agent_test
from ada_dev_py_ai.models import ListStoryModel, ListTestModel, ProjectModel, RequirementModel


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


def task_create_project_plan(input: str):
    return Task(
        description='Create a comprehensive project plan for the following requirements ' + input,
        expected_output="""
        a detailed project plan covering all phases of the project lifecycle
        the output should be a text with a list of project phases and deliverables
        the output language should be in portuguese (pt-br)
        """,
        output_json=ProjectModel,  # Assuming a similar model structure
        agent=agent_project_manager(input),
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


def task_map_business_rules(input: str):
    return Task(
        description='Mapear as regras de negócio implementadas no código fonte para ' + input,
        expected_output="""
        um relatório detalhado das regras de negócio implementadas no sistema
        o output deve ser um documento estruturado que descreve as regras de negócio e como elas são aplicadas no código
        a linguagem de saída deve ser em português (pt-br)
        """,
        output_json=RequirementModel,
        agent=agent_developer(input),
    )


def task_remap_application(input: str):
    return Task(
        description='Remap the application to identify implemented requirements and architecture for ' + input,
        expected_output="""
        a detailed report of the application's current architecture and implemented requirements
        the output should be a structured document outlining the system's components and their interactions
        the output language should be in portuguese (pt-br)
        """,
        output_json=RequirementModel,
        agent=agent_software_architect(input),
    )
