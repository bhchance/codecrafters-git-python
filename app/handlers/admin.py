from pathlib import Path

import constants


def handle_init():
    Path.mkdir(constants.GIT_PATH)
    Path.mkdir(constants.GIT_OBJECTS_PATH)
    Path.mkdir(constants.GIT_REFS_PATH)
    with open(constants.GIT_PATH / "HEAD") as f:
        f.write("ref: refs/heads/main\n")
