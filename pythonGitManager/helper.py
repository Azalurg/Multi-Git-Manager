import os


def initiate():
    path = "../data/paths.txt"
    isdir = os.path.isdir("../data/")
    isfile = os.path.isfile(path)

    if not isdir:
        os.mkdir("../data")

    if not isfile:
        with open(path, 'w'):
            pass

