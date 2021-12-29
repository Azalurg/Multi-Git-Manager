import actions
from termcolor import colored


def main():
    print(colored("===== Welcome to git-python-manager =====", "cyan"))
    print("To see all commands type 'help'")
    command = ""
    while command != "exit" and command != "close":
        command = input(">>> ")
        if command in actions.actions.keys():
            actions.actions[command]["function"]()


main()
