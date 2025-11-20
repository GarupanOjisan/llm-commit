# llm-commit

`llm-commit` is a CLI tool that automatically generates appropriate commit messages using Large Language Models (LLMs) based on your staged changes. It supports multiple providers like OpenAI, Anthropic, Google Gemini, and Ollama.

## Installation

### Prerequisites
- Python 3.12 or higher
- Git

### Install via Script
```bash
./install.sh
```

### Manual Installation
```bash
pip install .
```

## Configuration

Create a configuration file at `~/.config/llm-commit/config.yaml` or `.llm-commit.yaml` in your project root.

Example configuration:

```yaml
provider: openai # Options: openai, anthropic, gemini, ollama
language: en # Options: en, ja, etc.

providers:
  openai:
    api_key: your-api-key
    model: gpt-4o
  anthropic:
    api_key: your-api-key
    model: claude-3-5-sonnet-20240620
  gemini:
    api_key: your-api-key
    model: gemini-1.5-pro
  ollama:
    base_url: http://localhost:11434
    model: llama3
```

## Usage

1.  Stage your changes using git:
    ```bash
    git add .
    ```

2.  Run the tool:
    ```bash
    llm-commit
    ```

3.  The tool will analyze your changes and propose a commit message. You can:
    -   **Commit**: Accept the message and commit.
    -   **Edit**: Modify the message before committing.
    -   **Regenerate**: Ask the LLM for a new suggestion.
    -   **Cancel**: Exit without committing.

## License

MIT
