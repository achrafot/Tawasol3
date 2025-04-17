import openai
import requests

class PromptTransformer:
    @staticmethod
    def upload_reference_image(url: str) -> str:
        """
        Downloads the image from the given URL and uploads it to OpenAI,
        returning the file ID to be used as reference for image generation.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            image_bytes = response.content

            upload = openai.files.create(
                file=("reference.png", image_bytes, "image/png"),
                purpose="vision"
            )
            return upload["id"]

        except Exception as e:
            print(f"Failed to upload reference image: {e}")
            return None

    @staticmethod
    def transform_prompt(concept: str, language: str, referenced_image_id: str = None) -> dict:
        """
        Builds a DALL·E-style image generation prompt for PECS symbols,
        strictly following the Tawasol Symbols visual style — without GPT,
        and optionally uses a reference image for style consistency.
        """

        # Clean input
        concept_clean = concept.strip().capitalize()
        lang = language.lower()

        # Base prompt
        prompt = (
            f"A flat, two-dimensional digital illustration in the style of educational communication symbols. "
            f"It shows a cheerful Gulf Arab boy wearing a traditional white thobe and ghutra, expressing the concept: '{concept_clean}'. "
            f"The illustration follows these visual rules: bold black outlines, no shadows or gradients, no 3D effects, and a clean white background. "
            f"The concept should be represented with a simple, culturally appropriate object or symbol (e.g., red cross for hospital, plate of food, etc.). "
            f"The image must be minimalist, centered, and suitable for use in visual communication boards. "
            f"No text or captions should be included."
        )

        # Style reference note
        if referenced_image_id:
            prompt += (
                " Match the visual style (line weight, color palette, character design) "
                "of the attached reference image exactly."
            )

        return {
            "prompt": prompt,
            "referenced_image_ids": [referenced_image_id] if referenced_image_id else []
        }
