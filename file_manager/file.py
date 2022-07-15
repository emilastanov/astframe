
def make_file(name: str, path="", text="") -> None:
    """
    Make file with text.
    :param name: name of file.
    :param path: path of file.
    :param text: text of file.
    :return:
    """
    file = open(f"{path}/{name}", "w")
    file.write(text)
    file.close()
    print(f'astframe: File .{path}/{name} created.')


def append_to_file(name: str, path="", text="") -> None:
    """
    Append text into exist file.
    :param name: name of file.
    :param path: path of file.
    :param text: text of file.
    :return:
    """
    file = open(f"{path}/{name}", "a")
    file.write(text)
    file.close()
    print(f'astframe: Text has been appended in file {path}/{name}.')


def append_import_to_file(name: str, path="", importing="") -> None:
    """
    Append import to file.
    :param name: name of file.
    :param path: path of file.
    :param importing: importing header.
    :return:
    """
    file = open(f"{path}/{name}", "r")
    text = file.read()
    file.close()

    file = open(f"{path}/{name}", "w")
    file.write(f"{importing}\n{text}")
    file.close()
    print(f'astframe: Import has been appended in file {path}/{name}.')


def remove_text_from_file(name: str, path="", text="") -> None:
    """
       Append import to file.
       :param name: name of file.
       :param path: path of file.
       :param text: importing header.
       :return:
       """
    file = open(f"{path}/{name}", "r")
    file_text = file.read()
    file.close()

    file_text = file_text.replace(text, "")

    file = open(f"{path}/{name}", "w")
    file.write(file_text)
    file.close()
    print(f'astframe: Import has been removed from file {path}/{name}.')


def append_text_to_file_after_specified_string(name: str, specify_string: str, path="", text="") -> None:
    """
    Append text to file after specified string.
    :param name: name of file.
    :param specify_string: specified string.
    :param path: path of file.
    :param text: text of file.
    :return:
    """
    file = open(f"{path}/{name}", "r")
    text_of_file = file.read().replace('pass', '')
    file.close()

    begin_of_text = text_of_file[0:text_of_file.find(specify_string) + len(specify_string)]
    end_of_text = text_of_file[text_of_file.find(specify_string) + len(specify_string) + 1:]

    count_of_space = 0
    while end_of_text[count_of_space] == ' ':
        count_of_space += 1

    file = open(f"{path}/{name}", "w")
    file.write(f"{begin_of_text}\n{' ' * count_of_space}{text}\n{end_of_text}")
    file.close()
    print(f'astframe: Text has been appended in file {path}/{name} after specified string.')
