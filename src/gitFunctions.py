import git


def read():
    with open("../env/directories.txt", "r") as file:
        repos = []
        for line in file:
            repo = git.Repo(line)
            repos.append(repo)
    return repos


def untracked_files(repos):
    for repo in repos:
        file_list = repo.untracked_files
        print(repo, file_list)


def pull_project(self):
    success, error = True, None
    try:
        repo = git.Repo(self)
        remote = repo.remote()
        remote.pull()
    except Exception as e:
        success = False
        error = e
    return success, error


def show_status(self):
    success, error = True, None
    try:
        repo = git.Repo(self)
        if repo.index.diff(None) and repo.untracked_files:
            print("--------------------------------------------------------")
            print(self[:-1])
            print(repo.git.status(), '\n')
        else:
            pass
    except Exception as e:
        success = False
        error = e
    return success, error


def push_all(self):
    success, error = True, None
    try:
        repo = git.Repo(self)
        remote = repo.remote()
        remote.push()
    except Exception as e:
        success = False
        error = e
    return success, error
