"""
Tests for PromptBuilder.
"""
import unittest
from llm_commit.prompt_builder import PromptBuilder


class TestPromptBuilder(unittest.TestCase):
    """
    Test cases for PromptBuilder.
    """
    def test_build_en(self):
        """Test building English prompt."""
        builder = PromptBuilder(language="en")
        diff = "diff --git a/file.txt b/file.txt"
        prompt = builder.build(diff)
        self.assertIn("You are an experienced programmer", prompt)
        self.assertIn(diff, prompt)

    def test_build_ja(self):
        """Test building Japanese prompt."""
        builder = PromptBuilder(language="ja")
        diff = "diff --git a/file.txt b/file.txt"
        prompt = builder.build(diff)
        self.assertIn("あなたは熟練したプログラマーです", prompt)
        self.assertIn(diff, prompt)


if __name__ == "__main__":
    unittest.main()
