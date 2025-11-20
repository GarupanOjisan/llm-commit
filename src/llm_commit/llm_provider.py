from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    def generate_commit_message(self, prompt: str) -> str:
        """Generates a commit message based on the given prompt."""
        pass
