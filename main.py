from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os
from typing import List, Optional

app = FastAPI()

# ---------- MODELOS ----------

class PerguntaConsulta(BaseModel):
    texto: str

class IdeiaMusical(BaseModel):
    estilo: str
    vibe: Optional[str] = None
    referencias: Optional[List[str]] = []
    voz: Optional[str] = None

# ---------- ROTAS ----------

@app.get("/")
def root():
    return {
        "status": "MusicAi backend online",
        "message": "Servidor rodando com sucesso 🎶"
    }

@app.post("/chat/consulta")
def chat_consulta(pergunta: PerguntaConsulta):
    return {
        "tipo": "consulta",
        "pergunta": pergunta.texto,
        "resposta": "Resposta de teoria musical virá por IA em breve 🎵"
    }

@app.post("/chat/ideias")
def chat_ideias(ideia: IdeiaMusical):
    return {
        "tipo": "ideia_criativa",
        "tom_sugerido": "G",
        "campo_harmonico": ["G", "Am", "Bm", "C", "D", "Em"],
        "escala": ["G", "A", "B", "C", "D", "E", "F#"],
        "dica_melodica": "Use frases descendentes e notas longas no refrão para reforçar a nostalgia.",
        "entrada_usuario": ideia
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
