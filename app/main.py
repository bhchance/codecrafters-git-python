import sys

from handlers.admin import handle_init
from handlers.file import handle_read_file, handle_hash_file
from handlers.tree import handle_ls_tree


def main():
    # TODO: replace sys.argv with click
    command = sys.argv[1]

    match command:
        case "init":
            handle_init()
            print("Initialized git directory")

        case "cat-file":
            if sys.argv[2] != "-p":
                # TODO: tighten up error handling of illegal flags. Easier after moving to click
                # Only one TODO, applies to all entrypoints
                ...
            object_sha = sys.argv[3]
            header, content = handle_read_file(object_sha)
            print(content, end="")
        case "hash-object":
            filename_to_hash = sys.argv[3]
            write_file = sys.argv[2] == "-w"
            object_hash = handle_hash_file(filename_to_hash, write_file)
            print(object_hash)

        case "ls-tree":
            if sys.argv[2] == "--name-only":
                tree_sha = sys.argv[3]
                _, nodes = handle_ls_tree(tree_sha, name_only=True)
                for node in nodes:
                    print(node)

        case "write-tree":
            raise NotImplementedError

        case _:
            raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
