from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
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
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz") 
async def healthz():
    return {"status": "ok"}

@app.post("/api/generate-image", response_model=ImageResponse)
async def generate_image(request: ImageRequest, settings=Depends(get_settings)):
    try:
        client = OpenAI(api_key=settings.openai_api_key)

        # Step 1: Upload reference image for Tawasol Symbols style
        reference_url = "https://cdn.tawasol.mada.org.qa/data/wp-content/uploads/2021/10/HOMEPAGE-SYMBOLS-01-1-1200x945.png"
        reference_id = PromptTransformer.upload_reference_image(reference_url)

        # Step 2: Generate prompt with optional reference
        result = PromptTransformer.transform_prompt(
            concept=request.concept,
            language=request.language,
            referenced_image_id=reference_id
        )

        prompt = result["prompt"]
        referenced_ids = result["referenced_image_ids"]

        if not prompt:
            raise HTTPException(status_code=400, detail="Generated prompt is empty or invalid.")

        print(f"[Prompt Used] {repr(prompt)}")
        print(f"[Reference ID] {referenced_ids}")

        # Step 3: Generate image using DALL·E 3
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url

        return ImageResponse(
            image_url=image_url, 
            prompt_used=prompt
        )

    except Exception as e:
        print(f"[Error] {str(e)}")
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")