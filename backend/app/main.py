from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import psycopg
import openai
from openai import OpenAI
from dotenv import load_dotenv

from app.config import get_settings
from app.models import ImageRequest, ImageResponse
from app.prompt_transformer import PromptTransformer

load_dotenv()

app = FastAPI()

# Disable CORS. Do not remove this for full-stack development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.post("/api/generate-image", response_model=ImageResponse)
async def generate_image(request: ImageRequest, settings=Depends(get_settings)):
    try:
        client = OpenAI(api_key=settings.openai_api_key)
        
        transformed_prompt = PromptTransformer.transform_prompt(
            concept=request.concept,
            language=request.language
        )
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=transformed_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        image_url = response.data[0].url
        
        return ImageResponse(
            image_url=image_url,
            prompt_used=transformed_prompt
        )
    except openai.OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
