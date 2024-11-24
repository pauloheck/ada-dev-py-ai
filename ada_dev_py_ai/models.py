from pydantic import BaseModel


class RequirementModel(BaseModel):
    """
    Model representing a requirement with its title, detailed requirements, and acceptance criteria.
    """

    title: str
    requirements: str
    acceptance_criteria: str


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


class KPIModel(BaseModel):
    kpi_id: str
    name: str
    description: str
    target_value: float
    current_value: float
    status: str


class RiskModel(BaseModel):
    risk_id: str
    description: str
    impact: str
    probability: str
    mitigation_plan: str


class ProjectModel(BaseModel):
    title: str
    scope: str
    stakeholders: list[str]
    feasibility: str
    project_schedule: str
    communication_plan: str
    risks: list[RiskModel]
    risk_management_plan: str
    team: list[str]
    performance_kpis: list[KPIModel]
    budget_plan: str
    quality_plan: str
