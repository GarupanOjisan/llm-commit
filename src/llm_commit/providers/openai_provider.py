"""
OpenAI provider implementation.
"""
from openai import OpenAI
from ..llm_provider import LLMProvider


class OpenAIProvider(LLMProvider):
    """
    Provider for OpenAI API.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, api_key: str, model: str = "gpt-4o"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate_commit_message(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise RuntimeError(f"OpenAI API Error: {e}") from e
