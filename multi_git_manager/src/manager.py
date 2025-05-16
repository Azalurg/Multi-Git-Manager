from os import PathLike
from pathlib import Path
from typing import List, Dict
from datetime import datetime
from git import GitCommandError

from multi_git_manager.src.config_handler import ConfigHandler
from multi_git_manager.src.repository import Repository, ShortStatus


class Manager:
    """
    Class created to directly manage the repositories, as well as the configuration.
    You can think of it as a backend of the regular web application where each available function is and api endpoint available for your frontend.
    """

    def __init__(self, config_handler: 'ConfigHandler'):
        self.repositories: List[Repository] = []
        self.config_handler = config_handler
        self.import_repositories()

    def import_repositories(self) -> bool:
        """Gets the repositories from the config and loads them into the manager."""
        repo_paths = self.config_handler.get_repositories()
        for path in repo_paths:
            try:
                repo = Repository(Path(path))
                self.repositories.append(repo)
                print(f"Loaded repository: {path}")
            except Exception as e:
                print(f"Failed to load repository: {path}\n{e}")
                return False
        return True


    def add_repository(self, path: PathLike) -> Repository | None:
        """Add a repository to the manager and config."""
        if self.config_handler.add_repository(path):
            repo = Repository(path)
            self.repositories.append(repo)
            print(f"Added repository: {path}")
            return repo
        else:
            return None



    def remove_repository(self, path: PathLike) -> bool:
        """Remove a repository from the manager and config."""
        if self.config_handler.remove_repository(path):
            path_str = str(path)
            for repo in self.repositories:
                if repo.path == path_str:
                    self.repositories.remove(repo)
                    print(f"Removed repository: {path}")
                    return True
            print(f"Repository {path} not found in manager.")
            self.import_repositories()
            return True
        print(f"Failed to remove repository {path} from config.")
        return False

    # TODO: continue down

    def list_repositories(self) -> List[Repository]:
        return self.repositories

    def refresh_all(self) -> None:
        """Refresh the status of all repositories."""
        print("Refreshing status for all repositories...")
        for repo in self.repositories:
            repo.refresh()

        print(f"All repositories refreshed ({len(self.repositories)})")


    def pull_all(self) -> None:
        """Pull updates for all repositories from their remote branches."""
        print("Pulling updates for all repositories...")
        for repo in self.repositories:
            try:
                print(f"Pulling {repo.name} ({repo.active_branch}) from {repo.origin_branch}...")
                repo.git_pull()
                status = repo.get_short_status()
                print(f"Pulled {repo.name}: {status}")
            except GitCommandError as e:
                print(f"Error pulling {repo.name}: {e}")
            except Exception as e:
                print(f"Unexpected error pulling {repo.name}: {e}")
        print(f"All repositories pulled successfully ({len(self.repositories)})")

    def push_all(self) -> None:
        """Push changes for all repositories to their remote branches."""
        print("Pushing changes for all repositories...")
        for repo in self.repositories:
            try:
                print(f"Pushing {repo.name} ({repo.active_branch}) to {repo.origin_branch}...")
                repo.git_push()
                status = repo.get_short_status()
                print(f"Pushed {repo.name}: {status}")
            except GitCommandError as e:
                print(f"Error pushing {repo.name}: {e}")
            except Exception as e:
                print(f"Unexpected error pushing {repo.name}: {e}")
        print(f"All repositories pushed successfully ({len(self.repositories)})")

    def commit_all(self, message: str | None = None) -> None:
        """Commit changes in all repositories with a custom or default message."""
        print("Committing changes for all repositories...")
        for repo in self.repositories:
            try:
                if repo.staged > 0:
                    print(f"Committing {repo.name} ({repo.active_branch})...")
                    repo.git_commit(message)
                    status = repo.get_short_status()
                    print(f"{repo.name} - Done!")
                else:
                    print(f"{repo.name} - No changes to commit.")
            except GitCommandError as e:
                print(f"Error committing {repo.name}: {e}")
            except Exception as e:
                print(f"Unexpected error committing {repo.name}: {e}")
        print("All repositories committed successfully.")

    def add_all_files(self) -> None:
        """Stage all changes (including untracked files) in all repositories."""
        print("Staging all changes in all repositories...")
        for repo in self.repositories:
            try:
                repo.git_add_all()
                print(f"Staged all in {repo}")
            except GitCommandError as e:
                print(f"Error staging files in {repo.name}: {e}")
            except Exception as e:
                print(f"Unexpected error staging files in {repo.name}: {e}")
        print("All repositories staged successfully.")

    def print_status_all(self) -> None:
        """Print the status of all repositories in a formatted way."""
        print("\nStatus of all repositories:")
        print("===========================")
        for repo in self.repositories.values():
            status = repo.get_short_status()
            print(f"{repo.name} ({repo.active_branch}): {status}")
        print("===========================")
