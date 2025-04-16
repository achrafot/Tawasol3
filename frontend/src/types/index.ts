export interface ImageGenerationRequest {
  concept: string;
  language: string;
}

export interface ImageGenerationResponse {
  image_url: string;
  prompt_used: string;
}
