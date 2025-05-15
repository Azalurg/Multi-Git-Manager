from pathlib import Path

from multi_git_manager.src.config_handler import ConfigHandler
from multi_git_manager.src.manager import Manager
from multi_git_manager.src.repository import Repository

if __name__ == "__main__":
    config = ConfigHandler("repo_config.json")
    repos_paths = config.get_repositories()

    for repo in repos_paths:
        print(Repository(Path(repo)))
