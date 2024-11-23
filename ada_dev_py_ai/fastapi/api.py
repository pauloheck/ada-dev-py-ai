from fastapi import FastAPI
from pydantic import BaseModel

from ada_dev_py_ai.crewai.create_story_ai import create_story_ai


class requesitoModel(BaseModel):
    titulo: str
    requisitos: str
    criterios_aceitacao: str


class storyModel(BaseModel):
    titulo: str
    descricao: str
    criterios_aceitacao: str


app = FastAPI()


@app.post('/story/create')
def create_story(input: requesitoModel):
    """
    Create a story for the developer, by the user input requirements.
    Input the row requirements and the story will be created.
    """
    print(f'input: {input}')
    return create_story_ai(input.input)


@app.get('/')
def root_start():
    return {'message': 'Hello, world!'}
