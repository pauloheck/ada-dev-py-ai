from fastapi import FastAPI, HTTPException

from ada_dev_py_ai.crewai.create_story_ai import create_story_ai

app = FastAPI()


@app.post('/story/create')
def create_story(input: str):
    """
    Create a story for the developer, by the user input requirements.
    Input the row requirements and the story will be created.
    """
    try:
        return create_story_ai(input)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
