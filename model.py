
def append_model(name: str, path: str) -> None:
    """
    Method for append model to model.py file.
    :param path:
    :param name: name of model.
    :return:
    """
    file = open(path + "/app/source/models.py", "a")
    file.write(
        "\n"
        "\n"
        f"class {name.capitalize()}(db.Model):\n"
        f"    __tablename__ = '{name.lower()}'\n"
        "    id = db.Column(db.Integer, primary_key=True)\n"
        "    title = db.Column(db.String, nullable=False)\n"
        "    name = db.Column(db.String)\n"
        "    description = db.Column(db.String)\n"
    )
    file.close()


def remove_model(name: str, path: str) -> None:
    """
        Method for append model to model.py file.
        :param path:
        :param name: name of model.
        :return:
        """
    file = open(path + "/app/source/models.py", "r")
    file_text = file.read()
    file.close()

    file_text = file_text.replace(
        "\n"
        "\n"
        f"class {name.capitalize()}(db.Model):\n"
        f"    __tablename__ = '{name.lower()}'\n"
        "    id = db.Column(db.Integer, primary_key=True)\n"
        "    title = db.Column(db.String, nullable=False)\n"
        "    name = db.Column(db.String)\n"
        "    description = db.Column(db.String)\n",
        ""
    )

    file = open(path + "/app/source/models.py", "w")
    file.write(file_text)
    file.close()