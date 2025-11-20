import argparse
import sys
import os
import subprocess
import tempfile
from typing import Optional

from .config import ConfigManager
from .git_client import GitClient
from .provider_factory import ProviderFactory
from .prompt_builder import PromptBuilder

def open_editor(content: str) -> str:
    """Opens the default editor to edit the content."""
    editor = os.environ.get("EDITOR", "vim")
    with tempfile.NamedTemporaryFile(suffix=".txt", mode="w+", delete=False) as tf:
        tf.write(content)
        tf_path = tf.name
    
    try:
        subprocess.call([editor, tf_path])
        with open(tf_path, "r") as tf:
            return tf.read().strip()
    finally:
        if os.path.exists(tf_path):
            os.remove(tf_path)

def main():
    parser = argparse.ArgumentParser(description="LLM Commit Message Generator")
    parser.add_argument("--diff", action="store_true", help="Show the diff that will be used")
    args = parser.parse_args()

    # 1. Initialize components
    config_manager = ConfigManager()
    config = config_manager.load_config()
    
    git_client = GitClient()
    
    # 2. Check git status
    if not git_client.is_inside_work_tree():
        print("Error: Not a git repository.")
        sys.exit(1)
        
    diff = git_client.get_diff()
    if not diff.strip():
        print("No staged changes found. Please stage your changes using 'git add'.")
        sys.exit(0)

    if args.diff:
        print("--- Staged Diff ---")
        print(diff)
        print("-------------------")

    # 3. Setup LLM and Prompt
    try:
        provider = ProviderFactory.create(config)
        language = config.get("language", "en")
        prompt_builder = PromptBuilder(language=language)
    except Exception as e:
        print(f"Configuration Error: {e}")
        print("Please check your config file.")
        sys.exit(1)

    print("Generating commit message...")
    
    # 4. Generation Loop
    current_message = ""
    while True:
        if not current_message:
            try:
                prompt = prompt_builder.build(diff)
                current_message = provider.generate_commit_message(prompt)
            except Exception as e:
                print(f"Generation Error: {e}")
                sys.exit(1)

        print("\n--- Generated Commit Message ---")
        print(current_message)
        print("--------------------------------")
        
        print("\nOptions:")
        print("[c]ommit      - Commit with this message")
        print("[e]dit        - Edit message in editor")
        print("[r]egenerate  - Generate a new message")
        print("[q]uit        - Cancel and exit")
        
        choice = input("\nAction [c/e/r/q]: ").lower().strip()
        
        if choice == 'c':
            try:
                git_client.commit(current_message)
                print("Successfully committed!")
                sys.exit(0)
            except Exception as e:
                print(f"Commit Error: {e}")
                sys.exit(1)
        elif choice == 'e':
            current_message = open_editor(current_message)
        elif choice == 'r':
            print("Regenerating...")
            current_message = "" # Clear to trigger regeneration
        elif choice == 'q':
            print("Aborted.")
            sys.exit(0)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
