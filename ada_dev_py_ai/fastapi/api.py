import openai
from config_openai import OPENAI_API_KEY, OPENAI_MODEL
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from ada_dev_py_ai.crewai.create_story_ai import create_story_ai


class requesitoModel(BaseModel):
    titulo: str
    requisitos: str
    criterios_aceitacao: str


class storyModel(BaseModel):
    titulo: str
    descricao: str
    criterios_aceitacao: str


class PromptModel(BaseModel):
    prompt: str = Field(..., example="Once upon a time...")


@app.post('/story/create')
def create_story(input: requesitoModel):
    """
    Create a story for the developer, by the user input requirements.
    Input the row requirements and the story will be created.
    """
    try:
    """
    print(f'input: {input}')
    return create_story_ai(input.input)


@app.get('/')
def root_start():
    return {'message': 'Hello, world!'}


# Inicializar o cliente OpenAI
openai.api_key = OPENAI_API_KEY


@app.post('/create-story')
def story(input: PromptModel):
    """
    Gera uma história baseada no prompt fornecido usando a API da OpenAI.
    """
    prompt = input.prompt
    """
    try:
        response = openai.Completion.create(engine=OPENAI_MODEL, prompt=prompt, max_tokens=150)
        story = response.choices[0].text.strip()
        return {'story': story}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
