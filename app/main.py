import hashlib
import sys
import os
import zlib
from pathlib import Path

NULL_BYTE = "\x00"
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
    elif command == "cat-file":
        if sys.argv[2] != "-p":
            #TODO: handle this
            ...
        object_hash = sys.argv[3]
        folder = object_hash[:2]
        filename = object_hash[2:]
        with open(git_objects_path/folder/filename, "rb") as f:
            data = zlib.decompress(f.read()).decode("utf-8")
            header, content = data.split(NULL_BYTE)
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
                output_folder = git_objects_path / folder
                output_folder.mkdir()
                output_path = git_objects_path / folder / filename
                with open(output_path, "wb") as output_f:
                    output_f.write(zlib.compress(output_data))

        if sys.argv[2] != "-w":
            #TODO: handle this
            ...

    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
