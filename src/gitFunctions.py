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
