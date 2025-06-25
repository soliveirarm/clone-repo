# Clone Repo

**_Simple python script for devs how want to automate the process of cloning your github repository, just type in the number of your repo (listed in terminal) and bam: you're done!_**

## Requirements

- [Python](https://www.python.org/downloads/) has to be installed
- Pip (usually comes with python)
- `requests` lib to make the requests to the Github API

  - To install it, just open up a terminal and type this:

    ```sh
    pip install requests
    ```

**: VS Code as your IDE (if you wanna open it with code after it's cloned, totally optional tho)

## How to use

1. Open `clone_repo.py` with VS Code (or another IDE of your preference)
2. Change the **`USERNAME`** constant to your own

   ```py
   USERNAME = "soliveirarm"  # change to your own username
   ```

3. Run it with **python**, that's it!

## Tweaks

- By default the reposity is saved in '`Desktop/Projects`', if you want to change the the **`PROJECTS_PATH`** constant to the path you want.

  ```py
  PROJECTS_PATH = f"{Path.home()}/Desktop/Projects"  # change if you want the clone repos on another folder
  ```

## Download the script

<a href="https://github.com/soliveirarm/clone-repo/releases/download/2.0/clone_repo.py">
    <img src="./github/download-button.png"/>
</a>

## Final Thoughts

- ChatGPT basically made this version for me, I'm quite lazy these days, sorryyy 😝
- If you see anything weird, please create an issue so I can solve it, thankss
