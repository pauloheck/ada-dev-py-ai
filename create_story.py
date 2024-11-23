import openai
from fastapi import FastAPI, HTTPException
from config_openai import OPENAI_API_KEY, OPENAI_MODEL

# Inicializar o cliente OpenAI
openai.api_key = OPENAI_API_KEY

app = FastAPI()

@app.post("/create-story/")
async def create_story(prompt: str):
    """
    Gera uma história baseada no prompt fornecido usando a API da OpenAI.
    """
    try:
        response = openai.Completion.create(
            engine=OPENAI_MODEL,
            prompt=prompt,
            max_tokens=150
        )
        story = response.choices[0].text.strip()
        return {"story": story}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
