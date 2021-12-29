import gitFunctions


def repos_list():
    with open("../env/directories.txt", "r") as file:
        for line in file:
            print(line, end="")


def close_app():
    pass


def print_help():
    for key, values in actions.items():
        print(str(key) + ": " + values["description"])


def add_directory():
    with open("../env/directories.txt", "a") as file:
        path = input("enter the path: ")
        file.write(path + "\n")


def delete_directory():
    print("Select number of line you want to delete")
    print("To delete all enter '000'")
    dir_list = []
    with open("../env/directories.txt", "r") as file:
        counter = 1
        for line in file:
            dir_list.append(line)
            print(str(counter) + ". " + line, end="")
            counter += 1
    decision = input("Enter your choice: ")
    if decision == "000":
        print("!!! YOU ARE ABOUT TO DELETE ALL PATHS !!!")
    else:
        try:
            decision = int(decision)
            if int(decision) <= len(dir_list):
                print("You are about to delete: " + dir_list[int(decision) - 1], end="")
            else:
                print("Wrong input")
                pass

        except ValueError:
            print("Wrong input")
            pass
    agriment = input("(Y/n) ")
    if agriment in ["Y", "y", "yes", "Yes", "YES"]:
        if decision == "000":
            file = open("../env/directories.txt", "w")
            file.close()
        else:
            dir_list.pop(int(decision - 1))
            file = open("../env/directories.txt", "w")
            for line in dir_list:
                file.write(line)
            file.close()


def pull_projects():
    counter = 0
    counter_errors = 0
    with open("../env/directories.txt", "r") as file:
        for line in file:
            success, error = gitFunctions.pull_project(line[:-1])
            counter += 1
            if success:
                print("OK - {}".format(line), end="")
            else:
                print("ERROR - {}".format(line), end="")
                counter_errors += 1
    print("You are up to date!")
    print("Pull operations done: {}/{}".format(counter - counter_errors, counter))


actions = {
    "help": {"description": "prints all available comands", "function": print_help},
    "exit": {"description": "exit script", "function": close_app},
    "close": {"description": "close script", "function": close_app},
    "list": {"description": "print list of directories of all repos", "function": repos_list},
    "add": {"description": "add patch to git project", "function": add_directory},
    "delete": {"description": "delete patch to git project", "function": delete_directory},
    "pull": {"description": "pull to all projects", "function": pull_projects}

}
