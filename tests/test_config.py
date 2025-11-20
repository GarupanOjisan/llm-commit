import unittest
import os
from pathlib import Path
from unittest.mock import patch, mock_open
from llm_commit.config import ConfigManager

class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.config_manager = ConfigManager()

    @patch("builtins.open", new_callable=mock_open, read_data="provider: openai\nlanguage: en")
    @patch("pathlib.Path.exists", return_value=True)
    def test_load_config(self, mock_exists, mock_file):
        config = self.config_manager.load_config()
        self.assertEqual(config["provider"], "openai")
        self.assertEqual(config["language"], "en")

    def test_merge_dicts(self):
        base = {"a": 1, "b": {"c": 2}}
        override = {"b": {"d": 3}, "e": 4}
        merged = self.config_manager._merge_dicts(base, override)
        expected = {"a": 1, "b": {"c": 2, "d": 3}, "e": 4}
        self.assertEqual(merged, expected)

    def test_get_value(self):
        self.config_manager.config = {"a": {"b": 1}}
        self.assertEqual(self.config_manager.get("a.b"), 1)
        self.assertIsNone(self.config_manager.get("a.c"))
        self.assertEqual(self.config_manager.get("a.c", "default"), "default")

if __name__ == "__main__":
    unittest.main()
