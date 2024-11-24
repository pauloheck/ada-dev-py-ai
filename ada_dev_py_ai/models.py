from pydantic import BaseModel


class requesitoModel(BaseModel):
    titulo: str
    requisitos: str
    criterios_aceitacao: str


class TestModel(BaseModel):
    test_case_id: str
    description: str
    steps: list[str]
    expected_result: str
    actual_result: str = None
    status: str = 'Not Executed'


class StoryModel(BaseModel):
    title: str
    context: str
    user_identification: str
    acceptance_criteria: str
    story_flow: str
    expected_result: str
