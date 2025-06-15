import hashlib
import sys
import os
import zlib
from pathlib import Path

git_objects_path = Path(".git/objects")

def main():

    command = sys.argv[1]
    if command == "init":
        Path.mkdir(Path(".git"))
        Path.mkdir(git_objects_path)
        Path.mkdir(Path(".git/refs"))
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")
    if command == "cat-file":
        if sys.argv[2] != "-p":
            #TODO: handle this
            ...
        object_hash = sys.argv[3]
        folder = object_hash[:2]
        filename = object_hash[2:]
        with open(git_objects_path / folder / filename, "rb") as f:
            data = zlib.decompress(f.read()).decode("utf-8")
            header, content = data.split("\x00")
            print(content, end="")
    if command == "hash-object":
        filename = sys.argv[3]
        with open(git_objects_path/filename) as f:
            object_hash = hashlib.sha1(f)
            print(object_hash)
        if sys.argv[2] != "-w":
            #TODO: handle this
            ...

    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
