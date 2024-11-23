from fastapi import FastAPI, HTTPException
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
    try:
        print(f'input: {input}')
        return create_story_ai({
            "titulo": input.titulo,
            "requisitos": input.requisitos,
            "criterios_aceitacao": input.criterios_aceitacao
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/')
def root_start():
    return {"message": "Hello, world!"}
