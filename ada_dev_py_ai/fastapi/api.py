from fastapi import FastAPI, HTTPException
from ada_dev_py_ai.fastapi.cors_config import add_cors_middleware

from ada_dev_py_ai.crewai.crew import create_story_ai

app = FastAPI()

# Configuração do CORS
add_cors_middleware(app)


@app.post('/story/create')
def create_story(input: str):
    """
    Create a story for the developer, by the user input requirements.
    Input the row requirements and the story will be created.
    """
    try:
        print('chamando a api ' + input)
        return create_story_ai(input)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
