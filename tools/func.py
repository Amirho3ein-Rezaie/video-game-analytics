from subprocess import run


def run_command(command: str) -> int:
    "run one command in terminal"
    try:
        run(command, shell=True)
        return 0
    except:
        return 1
