import { ImageGenerationRequest, ImageGenerationResponse } from '../types';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const generateImage = async (
  request: ImageGenerationRequest
): Promise<ImageGenerationResponse> => {
  try {
    const response = await fetch(`${API_URL}/api/generate-image`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Failed to generate image');
    }

    return await response.json();
  } catch (error) {
    if (error instanceof Error) {
      throw new Error(`Image generation failed: ${error.message}`);
    }
    throw new Error('Image generation failed');
  }
};
