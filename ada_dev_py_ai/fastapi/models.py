from pydantic import BaseModel

class requesitoModel(BaseModel):
    titulo: str
    requisitos: str
    criterios_aceitacao: str

class storyModel(BaseModel):
    titulo: str
    descricao: str
    criterios_aceitacao: str
