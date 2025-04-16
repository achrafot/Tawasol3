class PromptTransformer:
    """
    Transforms user input concepts into detailed prompts that follow the Tawasol Symbols style.
    """
    
    @staticmethod
    def transform_prompt(concept: str, language: str = "english") -> str:
        """
        Transform a user concept into a detailed prompt for image generation.
        
        Args:
            concept: The user input concept (e.g., "I want to eat")
            language: The language for the caption ("english" or "arabic")
            
        Returns:
            A detailed prompt following Tawasol Symbols style guidelines
        """
        base_template = (
            "This flat, two-dimensional digital illustration shows a cheerful Gulf Arab {gender} "
            "in traditional attire (white thobe and ghutra), {action_description}. "
            "The style follows Tawasol Symbols, with bold outlines, cultural attire, and a clean white background. "
            "{caption_text}"
        )
        
        gender = "boy"
        
        action_description = PromptTransformer._get_action_description(concept)
        
        caption_text = ""
        if language.lower() == "arabic":
            arabic_text = PromptTransformer._get_arabic_translation(concept)
            caption_text = f"Arabic text at the bottom reads: {arabic_text}"
        else:
            caption_text = f"Text at the bottom reads: '{concept}'"
        
        final_prompt = base_template.format(
            gender=gender,
            action_description=action_description,
            caption_text=caption_text
        )
        
        return final_prompt
    
    @staticmethod
    def _get_action_description(concept: str) -> str:
        """
        Maps common concepts to visual descriptions of actions.
        This can be expanded with more mappings as needed.
        """
        concept_lower = concept.lower()
        
        if "eat" in concept_lower or "food" in concept_lower:
            return "raising his hand to his mouth next to a simple plate of food"
        elif "drink" in concept_lower or "water" in concept_lower:
            return "holding a glass of water near his mouth"
        elif "go" in concept_lower or "walk" in concept_lower:
            return "walking with one foot forward, with a simple path ahead"
        elif "sleep" in concept_lower or "bed" in concept_lower:
            return "lying on a simple bed with eyes closed"
        elif "play" in concept_lower:
            return "playing with a simple toy with a joyful expression"
        elif "read" in concept_lower or "book" in concept_lower:
            return "holding an open book with focused attention"
        elif "write" in concept_lower:
            return "holding a pencil to paper on a simple desk"
        elif "talk" in concept_lower or "speak" in concept_lower:
            return "with his mouth open and a speech bubble nearby"
        elif "listen" in concept_lower or "hear" in concept_lower:
            return "with his hand cupped behind his ear in a listening pose"
        elif "baba" in concept_lower or "father" in concept_lower or "dad" in concept_lower:
            return "standing next to a taller Gulf Arab man in traditional attire representing his father"
        elif "mama" in concept_lower or "mother" in concept_lower or "mom" in concept_lower:
            return "standing next to a Gulf Arab woman in traditional attire representing his mother"
        else:
            return "performing the action with clear body language that represents the concept"
    
    @staticmethod
    def _get_arabic_translation(concept: str) -> str:
        """
        Returns Arabic translations for common concepts.
        This is a simplified implementation and would be expanded in a production system.
        """
        concept_lower = concept.lower()
        
        if "eat" in concept_lower:
            return "أريد أن آكل"
        elif "drink" in concept_lower:
            return "أريد أن أشرب"
        elif "go" in concept_lower:
            return "أريد أن أذهب"
        elif "sleep" in concept_lower:
            return "أريد أن أنام"
        elif "play" in concept_lower:
            return "أريد أن ألعب"
        elif "read" in concept_lower:
            return "أريد أن أقرأ"
        elif "write" in concept_lower:
            return "أريد أن أكتب"
        elif "talk" in concept_lower or "speak" in concept_lower:
            return "أريد أن أتحدث"
        elif "listen" in concept_lower:
            return "أريد أن أستمع"
        elif "baba" in concept_lower or "father" in concept_lower:
            return "أريد أن أذهب مع بابا"
        elif "mama" in concept_lower or "mother" in concept_lower:
            return "أريد أن أذهب مع ماما"
        else:
            return concept
