"""
Anthropic provider implementation.
"""
from anthropic import Anthropic
from ..llm_provider import LLMProvider


class AnthropicProvider(LLMProvider):
    """
    Provider for Anthropic API.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, api_key: str, model: str = "claude-3-5-sonnet-20240620"):
        """
        Initializes the Anthropic provider.
        """
        self.client = Anthropic(api_key=api_key)
        self.model = model

    def generate_commit_message(self, prompt: str) -> str:
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text.strip()
        except Exception as e:
            raise RuntimeError(f"Anthropic API Error: {e}") from e
