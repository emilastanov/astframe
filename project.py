from os import system
from sys import argv

from file_manager.dir import make_dir
from file_manager.file import make_file
from file_manager.gitignore import make_gitignore
from file_manager.python_dir import make_python_dir
from file_manager.requirements import make_requirements
from scripts.init.main import MAIN
from scripts.init.migrations import MIGRATIONS
from scripts.init.objects import INIT_FILE, CREATE, DELETE, QUERY, REQUEST, RESPONSE, UPDATE, \
    ATTRIBUTES
from scripts.init.config import CONFIG, SETTINGS
from scripts.init.database import ACCESSOR
from scripts.init.errors import ERRORS
from scripts.init.response import SUCCESS, FAILED
from scripts.init.schemas import SCHEMAS


def init(argv: argv, path) -> None:
    """
    Initialize project structure
    :return:
    """

    make_python_dir(path + '/app')
    make_dir('config')

    make_python_dir('source', path + '/app')

    make_python_dir('store', path + '/app')

    make_python_dir('views', path + '/app/source')
    make_python_dir('tests', path + '/app/source')

    make_python_dir('database', path + '/app/store')

    make_python_dir('data_formats', path + '/app/source')
    make_python_dir('middlewares', path + '/app')

    make_python_dir('objects', path + '/app/middlewares')

    make_gitignore()
    make_requirements()
    system('pip install --upgrade pip')
    system('pip install -r requirements.txt')

    make_file(
        '__init__.py',
        path=path + '/app/middlewares/objects',
        text=INIT_FILE
    )

    make_file(
        'create.py',
        path=path + '/app/middlewares/objects',
        text=CREATE
    )

    make_file(
        'delete.py',
        path=path + '/app/middlewares/objects',
        text=DELETE
    )

    make_file(
        'query.py',
        path=path + '/app/middlewares/objects',
        text=QUERY
    )

    make_file(
        'request.py',
        path=path + '/app/middlewares/objects',
        text=REQUEST
    )

    make_file(
        'response.py',
        path=path + '/app/middlewares/objects',
        text=RESPONSE
    )

    make_file(
        'errors.py',
        path=path + '/app/middlewares',
        text=ERRORS
    )

    make_file(
        'update.py',
        path=path + '/app/middlewares/objects',
        text=UPDATE
    )

    make_file(
        'attributes.py',
        path=path + '/app/middlewares/objects',
        text=ATTRIBUTES
    )

    make_file(
        'models.py',
        path=path + '/app/store/database',
        text="from gino import Gino\n\n"
             "db = Gino()\n"
    )

    make_file(
        'success.py',
        path=path + '/app/source/data_formats',
        text=SUCCESS
    )

    make_file(
        'errors.py',
        path=path + '/app/source/data_formats',
        text=FAILED
    )

    make_file(
        '__init__.py',
        path=path + '/app/source/data_formats',
        text="from app.source.data_formats.errors import *\n"
             "from app.source.data_formats.success import *\n"
    )

    make_file(
        'accessor.py',
        path=path + '/app/store/database',
        text=ACCESSOR

    )

    make_file(
        'config.yaml',
        path=path + '/config',
        text=CONFIG
    )

    make_file(
        'settings.py',
        path=path + '/app',
        text=SETTINGS
    )

    make_file(
        'models.py',
        path=path + '/app/source',
        text="from sqlalchemy.dialects.postgresql import UUID\n"
             "from uuid import uuid4\n"
             "\n"
             "from app.store.database.models import db\n"
    )

    make_file(
        'routes.py',
        path=path + '/app/source',
        text=""
             "\n"
             "\n"
             "def setup_routes(app):\n"
             "    pass\n"
    )

    make_file(
        'schemas.py',
        path=path + '/app/source/views',
        text=SCHEMAS
    )

    make_file(
        'README.md',
        path=path,
        text=f'# {argv[2]}\n' if len(argv) > 2 else '# aiohttp_based_microservice\n'
    )

    make_file(
        'main.py',
        path=path,
        text=MAIN.format(title=argv[2] if len(argv) > 2 else 'Aiohttp based microservice.')
    )

    system("alembic init migrations")

    file = open(path + "/alembic.ini", "r")
    text = file.read().replace("driver://user:pass@localhost/dbname", "None")
    file.close()

    file = open(path + "/alembic.ini", "w")
    file.write(text)
    file.close()

    make_file(
        "env.py",
        path=path + "/migrations",
        text=MIGRATIONS
    )
