from commands import commands
from termcolor import colored
import helper


def main():
    helper.initiate()
    print(colored("===== Welcome to git-python-manager =====", "cyan"))
    print(colored("* To see all commands type 'help' *", "yellow"))
    command = ""
    while command != "exit" and command != "close":
        command = input(">>> ")
        if command in commands.keys():
            commands[command]["function"]()


main()
