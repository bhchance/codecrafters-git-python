import constants
from utils import read_git_object


def handle_ls_tree(tree_sha, name_only: bool):
    header, nodes = read_git_object(tree_sha, constants.GIT_OBJECT_TYPE.TREE)
    if name_only:
        names = []
        for _, name, _ in nodes:
            names.append(name)
        return names
    raise NotImplementedError
