import functions as f

commands = {
    "help": {"description": "print all available commands", "function": f.print_help},
    "exit": {"description": "exit script", "function": f.close_app},
    "close": {"description": "close script", "function": f.close_app},
    "list": {"description": "print list of paths", "function": f.print_all_paths},
    "add": {"description": "add patch to list", "function": f.add_path},
    "delete": {"description": "delete patch from list", "function": f.delete_path},
    "pull": {"description": "pull all projects", "function": f.projects_pull},
    "status": {"description": "show all status", "function": f.projects_status},
    "push": {"description": "push all commits", "function": f.projects_push},
    "commit": {"description": "commits all projects", "function": f.projects_commit},
}
