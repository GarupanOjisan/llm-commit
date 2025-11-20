"""
Configuration manager for llm-commit.
"""
import os
from pathlib import Path
from typing import Any, Dict

import yaml


class ConfigManager:
    """
    Manages configuration loading and merging.
    """
    def __init__(self):
        self.config: Dict[str, Any] = {}
        self.global_config_path = Path.home() / ".config" / "llm-commit" / "config.yaml"
        self.local_config_path = Path.cwd() / ".llm-commit.yaml"

    def load_config(self) -> Dict[str, Any]:
        """Loads and merges configuration from global and local files."""
        global_config = self._load_yaml(self.global_config_path)
        local_config = self._load_yaml(self.local_config_path)

        # Merge: local overrides global
        self.config = self._merge_dicts(global_config, local_config)
        return self.config

    def _load_yaml(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            return {}

        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            # Expand environment variables
            content = os.path.expandvars(content)

            return yaml.safe_load(content) or {}
        except (OSError, yaml.YAMLError) as e:
            # In a real app, we might want to log this
            print(f"Warning: Error loading config file {path}: {e}")
            return {}

    def _merge_dicts(self, base: Dict, override: Dict) -> Dict:
        """Deep merge two dictionaries."""
        result = base.copy()
        for k, v in override.items():
            if k in result and isinstance(result[k], dict) and isinstance(v, dict):
                result[k] = self._merge_dicts(result[k], v)
            else:
                result[k] = v
        return result

    def get(self, key: str, default: Any = None) -> Any:
        """Get a value from the config using dot notation."""
        keys = key.split(".")
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
            if value is None:
                return default
        return value
