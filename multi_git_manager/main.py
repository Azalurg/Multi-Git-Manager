from pathlib import Path

from multi_git_manager.src.config_handler import ConfigHandler
from multi_git_manager.src.manager import Manager

if __name__ == "__main__":
    config = ConfigHandler("repo_config.json")
    manager = Manager(config)
    manager.add_repository(Path("/home/azalurg/Github/Multi-Git-Manager"))
    repos = manager.list_repositories()

    for repo in repos:
        print(repo)
