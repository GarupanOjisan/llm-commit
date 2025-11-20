import subprocess
from typing import Optional

class GitClient:
    def is_inside_work_tree(self) -> bool:
        """Checks if the current directory is inside a git working tree."""
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--is-inside-work-tree"],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip() == "true"
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def get_diff(self) -> str:
        """Returns the staged diff."""
        try:
            result = subprocess.run(
                ["git", "diff", "--cached"],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to get git diff: {e.stderr}")

    def commit(self, message: str) -> None:
        """Commits the staged changes with the given message."""
        try:
            subprocess.run(
                ["git", "commit", "-m", message],
                check=True
            )
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to commit: {e}")
