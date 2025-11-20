from typing import Dict, Any
from .llm_provider import LLMProvider
from .providers.openai_provider import OpenAIProvider
from .providers.anthropic_provider import AnthropicProvider
from .providers.gemini_provider import GeminiProvider
from .providers.ollama_provider import OllamaProvider

class ProviderFactory:
    @staticmethod
    def create(config: Dict[str, Any]) -> LLMProvider:
        provider_name = config.get("provider", "openai")
        providers_config = config.get("providers", {})
        
        if provider_name == "openai":
            cfg = providers_config.get("openai", {})
            return OpenAIProvider(
                api_key=cfg.get("api_key"),
                model=cfg.get("model", "gpt-4o")
            )
        elif provider_name == "anthropic":
            cfg = providers_config.get("anthropic", {})
            return AnthropicProvider(
                api_key=cfg.get("api_key"),
                model=cfg.get("model", "claude-3-5-sonnet-20240620")
            )
        elif provider_name == "gemini":
            cfg = providers_config.get("gemini", {})
            return GeminiProvider(
                api_key=cfg.get("api_key"),
                model=cfg.get("model", "gemini-1.5-pro")
            )
        elif provider_name == "ollama":
            cfg = providers_config.get("ollama", {})
            return OllamaProvider(
                base_url=cfg.get("base_url", "http://localhost:11434"),
                model=cfg.get("model", "llama3")
            )
        else:
            raise ValueError(f"Unsupported provider: {provider_name}")
