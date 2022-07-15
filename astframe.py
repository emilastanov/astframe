#!/usr/bin/env python3
import os
from os import (
    system
)
from sys import argv

from object import make_object, remove_object
from project import init

path = os.getcwd()


def make_migrations(msg="") -> None:
    """
    Make migrations.
    :param msg: message
    :return:
    """
    system(f"alembic revision -m=\"{msg}\" --autogenerate")
    print(f'astframe: Migrations created.')


def migrate() -> None:
    """
    Migrate
    :return:
    """
    system("alembic upgrade head")
    print(f'astframe: Migrate has been made.')


def undo_migration() -> None:
    """
    Undo migrations
    :return:
    """
    system("alembic downgrade base")
    print(f'astframe: Last migrate has been undo.')


if __name__ == '__main__':
    try:
        command = argv[1]
    except IndexError:
        command = None

    if command == 'init':
        try:
            init(argv, path)
        except FileExistsError:
            print('astframe: Error: Some directory already exist. Folders /app and /config dirs must not exist.')
    elif command == 'make_object':
        if len(argv) > 2:
            try:
                make_object(argv[2], path)
            except FileNotFoundError as error:
                print(
                    'astframe: Error: Recently you must initialize project. Make command "python astproject.py init".')
        else:
            print('astframe: Error: Must specify the name of object as the second argument.')
    elif command == 'remove_object':
        if len(argv) > 2:
            try:
                remove_object(argv[2], path)
            except FileNotFoundError as error:
                print(
                    f'astframe: Error: Object "{argv[2]}" is not defined.')
        else:
            print('astframe: Error: Must specify the name of object as the second argument.')
    elif command == 'make_migrations':
        make_migrations(msg=argv[2] if len(argv) > 2 else "")
    elif command == 'migrate':
        migrate()
    elif command == 'undo_migration':
        undo_migration()
    else:
        print("""    AstFrame:
        Commands list:
        - init {Name of project (optional)}: Initialize project.
        - make_object "Object_name" {-idempotent (optional)}: Creating template of object.
        - make_migrations: Creating migrations for data base.
        - migrate: Migrate.
        - undo_migration: Undo last migrate.
        """)
