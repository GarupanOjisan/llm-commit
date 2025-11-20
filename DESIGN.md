# llm-commit

A CLI tool that automatically generates appropriate commit messages using LLMs (Large Language Models) based on changes in the Git staging area and performs commits.

## Features

- **Auto-generation**: Analyzes the content of `git diff --cached` and proposes commit messages tailored to the changes.
- **Multi-provider support**: Users can select their preferred LLM provider.
    - OpenAI (GPT-4o, GPT-3.5 Turbo etc.)
    - Anthropic (Claude 3.5 Sonnet etc.)
    - Google (Gemini 1.5 Pro etc.)
    - Ollama (Local LLMs)
- **Interactive Mode**: Allows not only committing the generated message as is but also editing or regenerating it.
- **Customization**: Prompt templates and output language (Japanese, English, etc.) can be configured.

## Design

### Architecture

This tool consists of the following modules:

1.  **Git Client**: Executes Git commands to retrieve diffs and perform commit operations.
2.  **Config Manager**: Manages user settings (provider selection, API keys, model settings, etc.).
3.  **LLM Provider Interface**: Abstracts different LLM providers to make them usable through a unified interface.
4.  **Prompt Builder**: Constructs input prompts for the LLM based on diff content and configured templates.

### Process Flow

1.  **Fetch Diff**: Executes `git diff --cached` to retrieve staged changes.
2.  **Build Prompt**: Combines the retrieved diff with pre-configured "instructions for commit message generation (system prompt)".
3.  **LLM Request**: Sends the prompt to the API of the configured provider (OpenAI, Gemini, etc.).
4.  **Generate Message**: Receives a draft commit message from the LLM.
5.  **User Confirmation**: Displays the generated message to the user.
    - **Commit**: Commits as is.
    - **Edit**: Edits the message before committing.
    - **Regenerate**: Regenerates another draft.
    - **Cancel**: Aborts the process.

### Configuration File (Example)

Managed in `~/.config/llm-commit/config.yaml` or `.llm-commit.yaml` in the project root.

```yaml
provider: openai # openai, anthropic, gemini, ollama
language: en # ja, en

providers:
  openai:
    api_key: ${OPENAI_API_KEY}
    model: gpt-4o
  anthropic:
    api_key: ${ANTHROPIC_API_KEY}
    model: claude-3-5-sonnet-20240620
  gemini:
    api_key: ${GEMINI_API_KEY}
    model: gemini-1.5-pro
  ollama:
    base_url: http://localhost:11434
    model: llama3
```

## Roadmap

- [ ] CLI implementation in Python
- [ ] Implementation of adapters for each provider
- [ ] Creation of installation script
