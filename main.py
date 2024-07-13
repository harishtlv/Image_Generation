from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import StableDiffusionPipeline
import torch
import os

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextToImageRequest(BaseModel):
    text: str

# Load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
model_id = "runwayml/stable-diffusion-v1-5"  # Make sure to replace with the correct model ID for SD3
pipeline = StableDiffusionPipeline.from_pretrained(model_id)
pipeline.to(device)

# Serve static files
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

@app.post("/generate-image")
async def generate_image(request: TextToImageRequest):
    try:
        # Generate the image
        image = pipeline(request.text).images[0]
        # Save the image
        image_path = "../frontend/generated_image.png"
        image.save(image_path)
        return {"image_url": "/static/generated_image.png"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Welcome to the Text to Image API!"}
