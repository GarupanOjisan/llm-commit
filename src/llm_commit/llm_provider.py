"""
Abstract base class for LLM providers.
"""
from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """
    Interface for LLM providers.
    """
    # pylint: disable=too-few-public-methods
    @abstractmethod
    def generate_commit_message(self, prompt: str) -> str:
        """Generates a commit message based on the given prompt."""
