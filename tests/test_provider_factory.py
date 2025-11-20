import unittest
from unittest.mock import MagicMock
import sys

# Mock external dependencies
sys.modules["openai"] = MagicMock()
sys.modules["anthropic"] = MagicMock()
sys.modules["google.generativeai"] = MagicMock()
sys.modules["requests"] = MagicMock()

from llm_commit.provider_factory import ProviderFactory
from llm_commit.providers.openai_provider import OpenAIProvider
from llm_commit.providers.anthropic_provider import AnthropicProvider

class TestProviderFactory(unittest.TestCase):
    def test_create_openai(self):
        config = {
            "provider": "openai",
            "providers": {
                "openai": {"api_key": "test", "model": "gpt-4"}
            }
        }
        provider = ProviderFactory.create(config)
        self.assertIsInstance(provider, OpenAIProvider)
        self.assertEqual(provider.model, "gpt-4")

    def test_create_anthropic(self):
        config = {
            "provider": "anthropic",
            "providers": {
                "anthropic": {"api_key": "test"}
            }
        }
        provider = ProviderFactory.create(config)
        self.assertIsInstance(provider, AnthropicProvider)

    def test_invalid_provider(self):
        config = {"provider": "unknown"}
        with self.assertRaises(ValueError):
            ProviderFactory.create(config)

if __name__ == "__main__":
    unittest.main()
