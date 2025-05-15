from datetime import datetime
from os import PathLike
from git import Repo, GitCommandError


class ShortStatus:
    def __init__(self, untracked: int, modified: int, staged: int, ahead: int, behind: int):
        self.untracked = untracked
        self.modified = modified
        self.staged = staged
        self.ahead = ahead
        self.behind = behind

    def __str__(self):
        message = ""
        if self.behind > 0 and self.ahead > 0:
            message += f"<{self.behind}, {self.ahead}> "
        elif self.behind > 0:
            message += f"<{self.behind} "
        elif self.ahead > 0:
            message += f"{self.ahead}> "

        if self.staged> 0:
            message += f"+{self.staged} "
        if self.modified > 0:
            message += f"!{self.modified} "
        if self.untracked > 0:
            message += f"?{self.untracked}"

        return message

class Repository:
    def __init__(self, path: PathLike, name: str | None = None):
        self.path = path
        self.name = name
        self.repo = None

        if self.name is None:
            self.name = self.path.__str__().split("/")[-1]

        self.untracked = 0
        self.modified = 0
        self.staged = 0
        self.ahead = 0
        self.behind = 0

        self.active_branch = None
        self.origin_branch = None

        self.refresh()

    def __str__(self):
        return f"{self.name} {self.active_branch} {self.get_short_status()}"

    def refresh(self):
        self.repo = Repo(self.path)

        self.untracked = len(self.repo.untracked_files)
        self.modified = len(self.repo.index.diff(None))
        self.staged = len(self.repo.index.diff("HEAD"))

        self.active_branch = self.repo.active_branch.name

        try:
            self.origin_branch = self.repo.active_branch.tracking_branch().name
        except (AttributeError, ValueError):
            self.origin_branch = f"origin/{self.active_branch}"

        try:
            merge_base = self.repo.merge_base(self.active_branch, self.origin_branch)[0]
            self.ahead = sum(1 for _ in self.repo.iter_commits(f"{merge_base.hexsha}..{self.active_branch}"))
            self.behind = sum(1 for _ in self.repo.iter_commits(f"{merge_base.hexsha}..{self.origin_branch}"))
        except (IndexError, ValueError) as e:

            print(f"Error calculating ahead/behind for {self.name}: {e}")
            self.ahead = 0
            self.behind = 0

    def get_short_status(self):
        return ShortStatus(self.untracked, self.modified, self.staged, self.ahead, self.behind)

    def git_pull(self):
        self.repo.git.pull()
        self.refresh()

    def git_push(self):
        self.repo.git.push()
        self.refresh()

    def git_commit(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.repo.git.commit("-m", f"Auto commit {dt_string}")
        self.refresh()

    def git_add_all(self):
        self.repo.git.add("--all")
        self.refresh()

    def git_add(self, path: str):
        try:
            self.repo.git.add(path)
        except GitCommandError as e:
            print(f"Error adding {path} to {self.name}: {e}")
        self.refresh()