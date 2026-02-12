from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os
from typing import List, Optional
from openai import OpenAI

app = FastAPI()

# ---------- CORS (LIBERA ACESSO DO LOVABLE) ----------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois podemos restringir ao domínio do app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- CONFIG OPENAI ----------

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
Você é um professor moderno especialista em teoria musical.

Responda sempre de forma:
- Clara
- Objetiva
- Didática
- Organizada visualmente

Regras obrigatórias:
- Máximo 8 linhas.
- Use emojis musicais quando fizer sentido (🎵🎶🎼).
- Separe blocos com linhas em branco.
- Evite símbolos como *, -, • ou numeração excessiva.
- Não escreva textos longos.
- Vá direto ao ponto.

Formato de resposta ideal:

🎼 Título do assunto

Explicação curta e direta.

🎵 Informações principais organizadas em linha separada.

Se houver fórmula ou sequência, escreva na mesma linha separada por traços.
"""

            },
            {
                "role": "user",
                "content": pergunta.texto
            }
        ],
        temperature=0.3
    )

    resposta_ia = response.choices[0].message.content

    return {
        "tipo": "consulta",
        "pergunta": pergunta.texto,
        "resposta": resposta_ia
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
