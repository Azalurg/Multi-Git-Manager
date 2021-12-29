import comands as c

actions = {
    "help": {"description": "print all available commands", "function": c.print_help},
    "exit": {"description": "exit script", "function": c.close_app},
    "close": {"description": "close script", "function": c.close_app},
    "list": {"description": "print list of paths", "function": c.print_all_paths},
    "add": {"description": "add patch to list", "function": c.add_path},
    "delete": {"description": "delete patch from list", "function": c.delete_path},
    "pull": {"description": "pull all projects", "function": c.projects_pull},
    "status": {"description": "show all status", "function": c.projects_status},
    "push": {"description": "push all commits", "function": c.projects_push},
    "commit": {"description": "commits all projects", "function": c.projects_commit}
}
