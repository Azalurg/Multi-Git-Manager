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
    list = []
    with open("../env/directories.txt", "r") as file:
        counter = 1
        for line in file:
            list.append(line)
            print(str(counter) + ". " + line, end="")
            counter += 1
    decision = input("Enter your choice: ")
    if decision == "000":
        print("!!! YOU ARE ABOUT TO DELETE ALL PATHS !!!")
    else:
        try:
            decision = int(decision)
            if int(decision) <= len(list):
                print("You are about to delete: " + list[int(decision) - 1],end="")
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
            list.pop(int(decision-1))
            file = open("../env/directories.txt", "w")
            for line in list:
                file.write(line)
            file.close()


actions = {
    "help": {"description": "prints all available comands", "function": print_help},
    "exit": {"description": "exit script", "function": close_app},
    "close": {"description": "close script", "function": close_app},
    "list": {"description": "print list of directories of all repos", "function": repos_list},
    "add": {"description": "add patch to git project", "function": add_directory},
    "delete": {"description": "delete patch to git project", "function": delete_directory}
}
