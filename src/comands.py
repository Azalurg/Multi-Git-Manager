def reposList():
    with open("../env/directories.txt", "r") as file:
        for line in file:
            print(line)


def closeApp():
    pass


def printHelp():
    for key, valuse in actions.items():
        print(str(key) + ": " + valuse["description"])


actions = {
    "help": {"description": "prints all available comands", "function": printHelp},
    "exit": {"description": "exit script", "function": closeApp},
    "close": {"description": "close script", "function": closeApp},
    "list": {"description": "print list of directories of all repos", "function": reposList},
}
