from os import mkdir
from shutil import rmtree


def make_python_dir(name: str, path="") -> None:
    """
    Make python directory.
    :param name: name of directory.
    :param path: path of directory.
    :return:
    """
    mkdir(f"{path}/{name}")
    open(f"{path}/{name}/__init__.py", "x")
    print(f'astframe: Python directory .{path}/{name} created.')


def drop_python_dir(name: str, path="") -> None:
    """
        Make python directory.
        :param name: name of directory.
        :param path: path of directory.
        :return:
        """
    rmtree(f"{path}/{name}")
    print(f'astframe: Python directory .{path}/{name} deleted.')
