"""
Module for building prompts for LLMs.
"""


class PromptBuilder:
    """
    Builds prompts for commit message generation.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, language: str = "en"):
        self.language = language

    def build(self, diff: str) -> str:
        """
        Constructs the full prompt including system instructions and the diff.
        """
        system_instruction = self._get_system_instruction()
        return f"{system_instruction}\n\nHere is the git diff:\n\n{diff}"

    def _get_system_instruction(self) -> str:
        if self.language == "ja":
            return (
                "あなたは熟練したプログラマーです。以下のgit diffに基づいて、"
                "簡潔で分かりやすいコミットメッセージを作成してください。"
                "Conventional Commitsの形式に従ってください (例: feat: add new feature)。"
                "出力はコミットメッセージのみにしてください。"
            )
        return (
            "You are an experienced programmer. Generate a concise and clear commit message "
            "based on the following git diff. "
            "Follow the Conventional Commits specification (e.g., feat: add new feature). "
            "Output only the commit message."
        )
