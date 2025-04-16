from pydantic import BaseModel


class ImageRequest(BaseModel):
    concept: str
    language: str = "english"


class ImageResponse(BaseModel):
    image_url: str
    prompt_used: str
