import zlib

import constants


def read_git_object(object_sha, object_type: constants.GIT_OBJECT_TYPE):
    folder_name = object_sha[:2]
    filename = object_sha[2:]
    with open(constants.GIT_OBJECTS_PATH / folder_name / filename, "rb") as f:
        data = zlib.decompress(f.read())

    if object_type == constants.GIT_OBJECT_TYPE.TREE:
        # Trees are a bit gnarly. So we find the null byte that indicates the separation
        # between mode/name and hash. Since the hash is a known 20 bytes, we can then
        # calculate the length of mode/name + 20 +spaces to slice of that part and keep parsing

        # Example format:
        # tree <size>\0
        # <mode> <name>\0 <20_byte_sha>
        # <mode> <name>\0 <20_byte_sha>
        header, tree_data = data.split(constants.NULL_BYTE, 1)
        nodes = []
        while tree_data:
            hash_starts = tree_data.find(constants.NULL_BYTE)
            mode, name = tree_data[:hash_starts].split()
            hash_ = tree_data[hash_starts + 1:hash_starts + 21]

            tree_data = tree_data[len(mode + b" " + name + b" " + hash_):]
            nodes.append((
                mode.decode(),
                name.decode(),
                hash_
            ))
        return header, nodes

    if object_type == constants.GIT_OBJECT_TYPE.FILE:
        header, content = data.split(constants.NULL_BYTE)
        return header.decode(), content.decode()
    raise NotImplementedError(f"Object type of {object_type} is not supported")
