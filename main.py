# main.py

from inference import generate_text
from fastapi import FastAPI, Query
from pydantic import BaseModel
from mangum import Mangum

app = FastAPI(title="TinyGPT Text Generation API")

class PredictResponse(BaseModel):
    generated_text: str
    prompt: str

@app.get("/predict", response_model=PredictResponse)
async def predict(
    prompt: str = Query("hello"),
    max_tokens: int = Query(15)
):
    generated_text = generate_text(prompt, max_tokens)
    return PredictResponse(
        generated_text=generated_text,
        prompt=prompt
    )

@app.get("/")
async def root():
    return {"message": "TinyGPT Text Generation API is running!"}

# Lambda handler
handler = Mangum(app)