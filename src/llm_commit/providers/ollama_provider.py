"""
Ollama provider implementation.
"""
import requests
from ..llm_provider import LLMProvider


class OllamaProvider(LLMProvider):
    """
    Provider for Ollama (local LLM).
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama3"):
        self.base_url = base_url
        self.model = model

    def generate_commit_message(self, prompt: str) -> str:
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=60
            )
            response.raise_for_status()
            return response.json().get("response", "").strip()
        except Exception as e:
            raise RuntimeError(f"Ollama API Error: {e}") from e
