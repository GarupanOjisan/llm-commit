import unittest
from llm_commit.prompt_builder import PromptBuilder

class TestPromptBuilder(unittest.TestCase):
    def test_build_en(self):
        builder = PromptBuilder(language="en")
        diff = "diff --git a/file.txt b/file.txt"
        prompt = builder.build(diff)
        self.assertIn("You are an experienced programmer", prompt)
        self.assertIn(diff, prompt)

    def test_build_ja(self):
        builder = PromptBuilder(language="ja")
        diff = "diff --git a/file.txt b/file.txt"
        prompt = builder.build(diff)
        self.assertIn("あなたは熟練したプログラマーです", prompt)
        self.assertIn(diff, prompt)

if __name__ == "__main__":
    unittest.main()
