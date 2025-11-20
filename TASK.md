# Implementation Tasks

## Phase 1: Project Setup & Core Infrastructure
- [x] Initialize Python project (setup `pyproject.toml` or `requirements.txt`)
- [x] Create project structure (`src/`, `tests/`)
- [x] Implement **Config Manager**
    - [x] Load config from `~/.config/llm-commit/config.yaml`
    - [x] Load config from `.llm-commit.yaml` (project root)
    - [x] Environment variable expansion support
- [x] Implement **Git Client**
    - [x] Function to get staged diff (`git diff --cached`)
    - [x] Function to commit with message (`git commit -m ...`)
    - [x] Check if git is installed and inside a repo

## Phase 2: LLM Integration
- [x] Define **LLM Provider Interface** (Abstract Base Class)
- [x] Implement **OpenAI Provider**
- [x] Implement **Anthropic Provider**
- [x] Implement **Gemini Provider**
- [x] Implement **Ollama Provider**
- [x] Implement **Prompt Builder**
    - [x] Create default system prompts
    - [x] Support language selection (en/ja)

## Phase 3: CLI & User Interaction
- [x] Implement Main CLI Entry Point
    - [x] Argument parsing
- [x] Implement Interactive Menu
    - [x] Display generated message
    - [x] Options: Commit, Edit, Regenerate, Cancel
    - [x] Edit functionality (open default editor)

## Phase 4: Polish & Distribution
- [x] Add error handling (API errors, no staged changes, etc.)
- [x] Write Unit Tests
- [x] Create installation script / instructions
