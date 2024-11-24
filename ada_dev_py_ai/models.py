from pydantic import BaseModel


class requesitoModel(BaseModel):
    titulo: str
    requisitos: str
    criterios_aceitacao: str


class TestModel(BaseModel):
    test_case_id: str
    description: str
    steps: str
    expected_result: str
    actual_result: str
    status: str


class ListTestModel(BaseModel):
    test_cases: list[TestModel]


class StoryModel(BaseModel):
    title: str
    context: str
    user_identification: str
    acceptance_criteria: str
    story_flow: str
    expected_result: str


class ListStoryModel(BaseModel):
    stories: list[StoryModel]


class ProjectModel(BaseModel):
    title: str
    scope: str
    stakeholders: list[str]
    feasibility: str
    project_schedule: str
    communication_plan: str
    risks: str
    risk_management_plan: str
    team: list[str]
    performance_kpis: str
    budget_plan: str
    quality_plan: str
