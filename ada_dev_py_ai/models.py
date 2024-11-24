from typing import Optional
from pydantic import BaseModel


class requesitoModel(BaseModel):
    titulo: str
    requisitos: str
    criterios_aceitacao: str


class TestModel(BaseModel):
    test_case_id: Optional[str] = None
    description: Optional[str] = None
    steps: Optional[list[str]] = None
    expected_result: Optional[str] = None
    actual_result: Optional[str] = None
    status: Optional[str] = 'Not Executed'


class StoryModel(BaseModel):
    title: str
    context: str
    user_identification: str
    acceptance_criteria: str
    story_flow: str
    expected_result: str
