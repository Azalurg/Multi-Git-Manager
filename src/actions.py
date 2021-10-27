import comands as c

actions = {
    "help": {"description": "print all available commands", "function": c.print_help},
    "exit": {"description": "exit script", "function": c.close_app},
    "close": {"description": "close script", "function": c.close_app},
    "list": {"description": "print list of directories of all repos", "function": c.print_all_paths},
    "add": {"description": "add patch to git project", "function": c.add_path},
    "delete": {"description": "delete patch to git project", "function": c.delete_path},
    "pull": {"description": "pull to all projects", "function": c.projects_pull},
    "status": {"description": "show status", "function": c.projects_status},
    "push": {"description": "push all commits", "function": c.projects_push},
    "commit": {"description": "commits all", "function": c.projects_commit}
}