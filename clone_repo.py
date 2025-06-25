import subprocess
from pathlib import Path
from os import path, makedirs, system
from time import sleep
import requests

PROJECTS_PATH = f"{Path.home()}/Desktop/Projects"  # change if you want the clone repos on another folder
USERNAME = "soliveirarm"  # change to your own username


def get_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch repos from GitHub. Check your username or network.")
        return []
    repos = response.json()
    return [repo["name"] for repo in repos]


def clone_repo():
    repos = get_repos()
    if not repos:
        print("No repos found or error occurred.")
        return

    print("\nAvailable Repos:")
    for i, repo in enumerate(repos, start=1):
        print(f"{i}. {repo}")

    while True:
        try:
            choice = int(input("\nEnter the number of the repo to clone:\n>> "))
            if 1 <= choice <= len(repos):
                REPO_NAME = repos[choice - 1]
                break
            else:
                print(f"Please choose a number between 1 and {len(repos)}")
        except ValueError:
            print("Invalid input, please enter a number.")

    if not path.exists(PROJECTS_PATH):
        makedirs(PROJECTS_PATH)

    GIT_CLONE_CMD = (
        f"cd {PROJECTS_PATH} && git clone https://github.com/{USERNAME}/{REPO_NAME}.git"
    )
    result = subprocess.run(GIT_CLONE_CMD, shell=True)

    if result.returncode == 0:
        print(f"\n✅ github.com/{USERNAME}/{REPO_NAME}.git cloned!\n")
        sleep(1)

        open_with_code = input("Do you want to open with code? (y/n): ").lower()
        if open_with_code == "y":
            print("Opening VS Code...")
            sleep(1)
            system(f"code {PROJECTS_PATH}/{REPO_NAME}")
    else:
        print(
            "❌ Clone failed! Double-check the repo name, your internet, or your GitHub access."
        )


if __name__ == "__main__":
    clone_repo()
