import json
import os
from os import PathLike
from pathlib import Path
from typing import List, Set


class ConfigHandler:
    """
    For now this component is mainly use to manage read and write git repositories to the json file.
    In the future the support for customisation and configuration may be added.
    """

    def __init__(self, config_path: str = "repo_config.json"):
        self._config_path = Path(config_path)
        self._config = {}
        self._paths_str: Set[str] = set()
        self._load_config()

    def _load_config(self) -> None:
        """Load the configuration from the JSON file and extract repositories paths."""
        try:
            if self._config_path.exists():
                with open(self._config_path, "r") as f:
                    self._config = json.load(f)
                print(f"Loaded configuration from {self._config_path}")
                self._paths_str = set(self._config["paths"])
            else:
                print(f"No config file found at {self._config_path}. Starting with empty config.")
                with open(self._config_path, "w") as f:
                    json.dump({"paths": []}, f, indent=4)
        except Exception as e:
            print(f"Error loading config: {e}")
            exit(1)

    def _save_config(self) -> bool:
        try:
            with open(self._config_path, "w") as f:
                json.dump(self._config, f, indent=4)
            print(f"Saved configuration to {self._config_path}")
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False

    def add_repository(self, path: PathLike) -> bool:
        path_str = str(path)
        self._paths_str.add(path_str)
        self._config["paths"] = list(self._paths_str)
        return self._save_config()

    def remove_repository(self, path: PathLike) -> bool:
        if str(path) not in self._paths_str:
            return False
        self._paths_str.remove(str(path))
        return self._save_config()

    def get_repositories(self) -> List[str]:
        repositories = list(self._paths_str)
        repositories.sort()
        return repositories
