import actions


def main():
    print("===== Welcome to git-python-manager =====")
    print("To see all commands type 'help'")
    comand = ""
    while comand != "exit" and comand != "close":
        comand = input(">>> ")
        if comand in actions.actions.keys():
            actions.actions[comand]["function"]()


main()
