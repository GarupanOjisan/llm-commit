"""
Gemini provider implementation.
"""
import google.generativeai as genai
from ..llm_provider import LLMProvider


class GeminiProvider(LLMProvider):
    """
    Provider for Google Gemini API.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, api_key: str, model: str = "gemini-1.5-pro"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)

    def generate_commit_message(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            raise RuntimeError(f"Gemini API Error: {e}") from e
