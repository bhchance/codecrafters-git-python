import sys
import os
from pathlib import Path


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    # Uncomment this block to pass the first stage

    command = sys.argv[1]
    if command == "init":
        Path.mkdir(Path(".git"))
        Path.mkdir(Path(".git/objects"))
        Path.mkdir(Path(".git/refs"))
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
