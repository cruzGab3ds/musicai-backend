from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Mensagem(BaseModel):
    texto: str

@app.get("/")
def inicio():
    return {"status": "MusicAí backend rodando"}

@app.post("/chat/consulta")
def chat_consulta(mensagem: Mensagem):
    return {
        "resposta": f"Você perguntou sobre teoria musical: {mensagem.texto}"
    }
