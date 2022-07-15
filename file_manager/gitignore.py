
def make_gitignore() -> None:
    """
    Make gitignore.
    """
    file = open(".gitignore", "w")
    file.write("/config/\n")
    file.write("/venv/\n")
    file.write("/migrations/\n")
    file.write("/app/tests/*.txt\n")
    file.close()
    print(f'astframe: .gitignore created.')
