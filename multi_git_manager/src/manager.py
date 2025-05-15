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



    def remove_repository(self, path: PathLike) -> bool:    # TODO: This method seams to be not the most efficient one
        """Remove a repository from the manager and config."""
        self.import_repositories()
        for i, repo in enumerate(self.repositories):
            if repo.path == path:
                self.config_handler.remove_repository(i)
                self.repositories.remove(repo)
                print(f"Removed repository: {path}")
                return True
        return False

    # TODO: continue down

    def list_repositories(self) -> List[Repository]:
        """Return a list of all managed repositories."""
        return list(self.repositories.values())

    def refresh_all(self) -> None:
        """Refresh the status of all repositories."""
        print("Refreshing status for all repositories...")
        for repo in self.repositories.values():
            try:
                repo.refresh()
                status = repo.get_short_status()
                print(f"Refreshed {repo.name} ({repo.active_branch}): {status}")
            except Exception as e:
                print(f"Error refreshing {repo.name}: {e}")

    def pull_all(self) -> None:
        """Pull updates for all repositories from their remote branches."""
        print("Pulling updates for all repositories...")
        for repo in self.repositories.values():
            try:
                print(f"Pulling {repo.name} ({repo.active_branch}) from {repo.origin_branch}...")
                repo.git_pull()
                status = repo.get_short_status()
                print(f"Pulled {repo.name}: {status}")
            except GitCommandError as e:
                print(f"Error pulling {repo.name}: {e}")
            except Exception as e:
                print(f"Unexpected error pulling {repo.name}: {e}")

    def push_all(self) -> None:
        """Push changes for all repositories to their remote branches."""
        print("Pushing changes for all repositories...")
        for repo in self.repositories.values():
            try:
                print(f"Pushing {repo.name} ({repo.active_branch}) to {repo.origin_branch}...")
                repo.git_push()
                status = repo.get_short_status()
                print(f"Pushed {repo.name}: {status}")
            except GitCommandError as e:
                print(f"Error pushing {repo.name}: {e}")
            except Exception as e:
                print(f"Unexpected error pushing {repo.name}: {e}")

    def commit_all(self, message: str | None = None) -> None:
        """Commit changes in all repositories with a custom or default message."""
        if message is None:
            now = datetime.now()
            message = f"Auto commit {now.strftime('%d/%m/%Y %H:%M:%S')}"
        print(f"Committing changes in all repositories with message: '{message}'...")
        for repo in self.repositories.values():
            try:
                if repo.modified > 0 or repo.staged > 0:
                    print(f"Committing {repo.name} ({repo.active_branch})...")
                    repo.repo.git.commit("-m", message)
                    repo.refresh()
                    status = repo.get_short_status()
                    print(f"Committed {repo.name}: {status}")
                else:
                    print(f"No changes to commit in {repo.name}")
            except GitCommandError as e:
                print(f"Error committing {repo.name}: {e}")
            except Exception as e:
                print(f"Unexpected error committing {repo.name}: {e}")

    def add_all_files(self) -> None:
        """Stage all changes (including untracked files) in all repositories."""
        print("Staging all changes in all repositories...")
        for repo in self.repositories.values():
            try:
                print(f"Staging all files in {repo.name} ({repo.active_branch})...")
                repo.git_add_all()
                status = repo.get_short_status()
                print(f"Staged all in {repo.name}: {status}")
            except GitCommandError as e:
                print(f"Error staging files in {repo.name}: {e}")
            except Exception as e:
                print(f"Unexpected error staging files in {repo.name}: {e}")

    def add_specific_file(self, repo_name: str, path: str) -> bool:
        """
        Stage a specific file in a specific repository.
        Returns True if successful, False if repository not found or operation fails.
        """
        if repo_name not in self.repositories:
            print(f"Repository {repo_name} not found")
            return False
        repo = self.repositories[repo_name]
        try:
            print(f"Staging file {path} in {repo.name} ({repo.active_branch})...")
            repo.git_add(path)
            status = repo.get_short_status()
            print(f"Staged {path} in {repo.name}: {status}")
            return True
        except GitCommandError as e:
            print(f"Error staging {path} in {repo.name}: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error staging {path} in {repo.name}: {e}")
            return False

    def get_repository_status(self, repo_name: str) -> ShortStatus | None:
        """
        Get the short status of a specific repository.
        Returns ShortStatus if found, None otherwise.
        """
        if repo_name in self.repositories:
            return self.repositories[repo_name].get_short_status()
        print(f"Repository {repo_name} not found")
        return None

    def print_status_all(self) -> None:
        """Print the status of all repositories in a formatted way."""
        print("\nStatus of all repositories:")
        print("===========================")
        for repo in self.repositories.values():
            status = repo.get_short_status()
            print(f"{repo.name} ({repo.active_branch}): {status}")
        print("===========================")
