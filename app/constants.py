from enum import Enum, auto
from pathlib import Path

NULL_BYTE = b"\x00"
GIT_PATH = Path(".git")
GIT_OBJECTS_PATH = GIT_PATH / "objects"
GIT_REFS_PATH = GIT_PATH / "refs"


class GIT_OBJECT_TYPE(Enum):
    FILE = auto()
    TREE = auto()
