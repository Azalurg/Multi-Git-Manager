from git import Repo, RemoteProgress
import gitFunctions
import comands
import os


def main():
    print("===== Welcome to git-python-manager =====")
    print("To see all commands type 'help'")
    comand = ""
    while comand != "exit" and comand != "close":
        comand = input(">>>")
        if comand in comands.actions.keys():
            comands.actions[comand]["function"]()


main()
