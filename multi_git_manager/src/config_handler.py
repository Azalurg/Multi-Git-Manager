import json
from os import PathLike
from pathlib import Path
from typing import List


class ConfigHandler:
    """
    For now this component is mainly use to manage read and write git repositories to the json file.
    In the future the support for customisation and configuration may be added.
    """
    def __init__(self, config_path: str = "repo_config.json"):
        self._config_path = Path(config_path)
        self._config = {}
        self._paths_str: List[str] = []
        self._load_config()

    def _load_config(self) -> None:
        """Load the configuration from the JSON file and extract repositories paths."""
        try:
            if self._config_path.exists():
                with open(self._config_path, 'r') as f:
                    self._config = json.load(f)
                print(f"Loaded configuration from {self._config_path}")
                self._paths_str = self._config["paths"]
            else:
                print(f"No config file found at {self._config_path}. Starting with empty config.")
        except Exception as e:
            print(f"Error loading config: {e}")
            exit(1)

    def _save_config(self) -> bool:
        try:
            with open(self._config_path, 'w') as f:
                json.dump(self._config, f, indent=4)
            print(f"Saved configuration to {self._config_path}")
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False

    def add_repository(self, path: PathLike) -> bool:   # TODO: improve this function
        path_str = str(path)
        self._paths_str.append(path_str)
        self._config["paths"] = self._paths_str
        return self._save_config()

    def remove_repository(self, position: int) -> bool: # TODO: improve this function
        if len(self._paths_str) < position:
            print(f"Position {position} out of range.")
            return False
        self._paths_str.pop(position)
        self._config["paths"] = self._paths_str
        return self._save_config()

    def get_repositories(self) -> List[str]:
        return self._paths_str
