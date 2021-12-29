from git import Repo, RemoteProgress


def read():
    with open("../env/directories.txt", "r") as file:
        repos = []
        for line in file:
            repo = Repo(line)
            repos.append(repo)
    return repos


def untracked_files(repos):
    for repo in repos:
        file_list = repo.untracked_files
        print(repo, file_list)
