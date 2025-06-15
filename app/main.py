import hashlib
import sys
import os
import zlib
from pathlib import Path

NULL_BYTE = "\x00"
GIT_OBJECTS_PATH = Path(".git/objects")

def read_git_object(object_sha, object_type):
    folder_name = object_sha[:2]
    filename = object_sha[2:]
    with open(GIT_OBJECTS_PATH/folder_name/filename, "rb") as f:
        data = zlib.decompress(f.read())

    if object_type == "tree":
        header, tree_data = data.split(b"\x00", 1)
        nodes = []
        while tree_data:
            hash_starts = tree_data.find(b"\x00")
            mode, name = tree_data[:hash_starts].split()
            hash_ = tree_data[hash_starts + 1:hash_starts + 21]

            tree_data = tree_data[len(mode + b" " + name + b" " + hash_):]
            nodes.append((
                mode.decode(),
                name.decode(),
                hash_
            ))
        return nodes
    else:
        header, content = data.decode().split("\x00")
        return header, content

def main():

    command = sys.argv[1]
    if command == "init":
        Path.mkdir(Path(".git"))
        Path.mkdir(GIT_OBJECTS_PATH)
        Path.mkdir(Path(".git/refs"))
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")
    elif command == "cat-file":
        if sys.argv[2] != "-p":
            #TODO: handle this
            ...
        object_hash = sys.argv[3]
        header, content = read_git_object(object_hash, "file")
        print(content, end="")
    elif command == "hash-object":
        filename_hash = sys.argv[3]
        with open(filename_hash, "rb", buffering=0) as f:

            f.seek(0)
            output_data = f.read().decode("utf-8")
            output_data = f"blob {os.stat(filename_hash).st_size}{NULL_BYTE}{output_data}".encode()
            object_hash = hashlib.sha1(output_data).hexdigest()
            print(object_hash)


            if sys.argv[2] == "-w":
                folder = object_hash[:2]
                filename = object_hash[2:]
                output_folder = GIT_OBJECTS_PATH / folder
                output_folder.mkdir()
                output_path = GIT_OBJECTS_PATH / folder / filename
                with open(output_path, "wb") as output_f:
                    output_f.write(zlib.compress(output_data))

        if sys.argv[2] != "-w":
            #TODO: handle this
            ...

    elif command == "ls-tree":
        if sys.argv[2] == "--name-only":
            tree_sha = sys.argv[3]
            nodes = read_git_object(tree_sha, "tree")
            for node in nodes:
                _, name, _ = node
                print(name)
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
