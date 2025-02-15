from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from ada_dev_py_ai.crewai.crew import create_project_plan_ai, create_story_ai, create_test_ai, remap_application

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Altere para os domínios permitidos
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.post('/test/create')
def create_test(input: str):
    """
    Create a test for the developer, by the user input requirements.
    Input the row requirements and the test will be created.
    """
    try:
        print('chamando a api ' + input)
        return create_test_ai(input)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post('/project/create')
def create_project(input: str):
    """
    Create a project plan for the developer, by the user input requirements.
    Input the row requirements and the project plan will be created.
    """
    try:
        print('chamando a api ' + input)
        return create_project_plan_ai(input)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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


@app.post('/business-rules/map')
def map_business_rules(input: str):
    """
    Map the business rules implemented in the source code based on user input.
    Input the raw requirements and the business rules mapping will be created.
    """
    try:
        print('Mapping business rules with input: ' + input)
        return remap_application(input)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
