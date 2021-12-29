import git
from datetime import datetime


def pull_all(self):
    success, error = True, None
    try:
        repo = git.Repo(self)
        remote = repo.remote()
        remote.pull()
    except Exception as e:
        success = False
        error = e
    return success, error


def status_all(self):
    success, error = True, None
    try:
        repo = git.Repo(self)
        if repo.index.diff(None) == repo.untracked_files:
            print("--------------------------------------------------------")
            print(self[:-1])
            print(repo.git.status(), '\n')
        else:
            print("Status - {}".format(self), end="")
    except Exception as e:
        success = False
        error = e
    return success, error


def push_all(self):
    success, error = True, None
    try:
        repo = git.Repo(self)
        repo.git.push()
    except Exception as e:
        success = False
        error = e
    return success, error


def commit_all_git(self):
    success, error = True, None
    try:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        repo = git.Repo(self)
        repo.git.add('--all')
        repo.git.commit('-m', "Auto commit done at {}".format(dt_string))
    except Exception as e:
        success = False
        error = e
    return success, error
