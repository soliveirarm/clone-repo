import subprocess
from pathlib import Path
from os import path, makedirs, system
from time import *

PROJECTS_PATH = f"{Path.home()}/Desktop/projects"
USERNAME = "soliveirarm"


def clone_repo():
    while True:
        REPO_NAME = input("Repository name: ")

        # creates the 'projects' folder if it does not exist
        if not path.exists(PROJECTS_PATH):
            makedirs(PROJECTS_PATH)

        GIT_CLONE_CMD = f"cd {PROJECTS_PATH} && git clone https://github.com/{USERNAME}/{REPO_NAME}.git"

        # runs the command on terminal
        subprocess.run(GIT_CLONE_CMD, shell=True)

        REPO_FOLDER = f"{PROJECTS_PATH}/{REPO_NAME}"

        # sees if the repo exists on github
        if path.exists(REPO_FOLDER):
            print(f"github.com/{USERNAME}/{REPO_NAME}.git cloned!\n")
            print("Your project is gonna open on VS Code...")
            sleep(1)
            system(f"code {REPO_FOLDER}")
            exit()
            break
        else:
            print(
                "The repository you tried to clone probably doesn't exist, try again\n"
            )
            sleep(1)


clone_repo()
