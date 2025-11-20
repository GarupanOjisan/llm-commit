"""
Tests for ProviderFactory.
"""
import unittest
from unittest.mock import MagicMock
import sys

# Mock external dependencies
sys.modules["openai"] = MagicMock()
sys.modules["anthropic"] = MagicMock()
sys.modules["google.generativeai"] = MagicMock()
sys.modules["requests"] = MagicMock()

# pylint: disable=wrong-import-position
from llm_commit.provider_factory import ProviderFactory
from llm_commit.providers.openai_provider import OpenAIProvider
from llm_commit.providers.anthropic_provider import AnthropicProvider


class TestProviderFactory(unittest.TestCase):
    """
    Test cases for ProviderFactory.
    """
    def test_create_openai(self):
        """Test creating OpenAI provider."""
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
        """Test creating Anthropic provider."""
        config = {
            "provider": "anthropic",
            "providers": {
                "anthropic": {"api_key": "test"}
            }
        }
        provider = ProviderFactory.create(config)
        self.assertIsInstance(provider, AnthropicProvider)

    def test_invalid_provider(self):
        """Test creating invalid provider."""
        config = {"provider": "unknown"}
        with self.assertRaises(ValueError):
            ProviderFactory.create(config)


if __name__ == "__main__":
    unittest.main()
