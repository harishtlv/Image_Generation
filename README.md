# Running the Application

## Install dependencies:

```bash
cd backend
pip install -r requirements.txt


## **Start the FastAPI server:**
uvicorn main:app --reload --host 0.0.0.0 --port 8000

This setup provides a complete web application for text-to-image
generation using FastAPI and Hugging Face's Stable Diffusion 3 model
