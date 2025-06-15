import hashlib
import os
import zlib

import constants
import utils


def handle_read_file(object_sha: str):
    header, content = utils.read_git_object(object_sha, constants.GIT_OBJECT_TYPE.FILE)
    return header, content


def handle_hash_file(filename, write_file: bool):
    with open(filename, "rb", buffering=0) as f:
        output_data = f.read().decode("utf-8")
        output_data = f"blob {os.stat(filename).st_size}{constants.NULL_BYTE.decode()}{output_data}".encode()
        object_hash = hashlib.sha1(output_data).hexdigest()

        if write_file:
            folder = object_hash[:2]
            filename = object_hash[2:]
            output_folder = constants.GIT_OBJECTS_PATH / folder
            output_folder.mkdir()
            output_path = constants.GIT_OBJECTS_PATH / folder / filename
            with open(output_path, "wb") as output_f:
                output_f.write(zlib.compress(output_data))

    return object_hash
