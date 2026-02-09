from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

# Modelo do que o usuário envia
class Pergunta(BaseModel):
    texto: str

# Rota raiz (já funcionando)
@app.get("/")
def root():
    return {
        "status": "MusicAi backend online",
        "message": "Servidor rodando com sucesso 🎶"
    }

# Rota de chat de consulta
@app.post("/chat/consulta")
def chat_consulta(pergunta: Pergunta):
    return {
        "pergunta": pergunta.texto,
        "resposta": "Você perguntou sobre música. Em breve isso será respondido por IA 🎵"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
