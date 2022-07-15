from os import mkdir


def make_dir(name: str, path="") -> None:
    """
    Make python directory.
    :param name: name of directory.
    :param path: path of directory.
    :return:
    """
    mkdir(f".{path}/{name}")
    print(f'astframe: Directory .{path}/{name} created.')
