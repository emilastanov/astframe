from scripts.objects.document_for_delete_method import make_document_for_delete_method
from scripts.objects.document_for_get_method import make_document_for_get_method
from scripts.objects.document_for_post_and_patch_method import make_document_for_post_and_patch_method
from scripts.objects.handler_for_delete_method import make_handler_for_delete_method
from scripts.objects.handler_for_get_method import make_handler_for_get_method
from scripts.objects.handler_for_patch_method import make_handler_for_patch_method
from scripts.objects.handler_for_post_method import make_handler_for_post_method
from scripts.objects.schemas import make_schema
from file_manager.file import make_file, append_to_file, append_import_to_file, \
    append_text_to_file_after_specified_string, remove_text_from_file
from file_manager.python_dir import make_python_dir, drop_python_dir
from model import append_model, remove_model


def make_object(name: str, path: str) -> None:
    """
    Make object with CRUD methods of rest api.
    :param path:
    :param name: name of object.
    :return:
    """
    make_python_dir(
        name.lower(),
        path=path + '/app/source/views'
    )

    make_python_dir(
        'methods',
        path=f'{path}/app/source/views/{name.lower()}'
    )

    make_python_dir(
        'delete',
        path=f'{path}/app/source/views/{name.lower()}/methods'
    )

    make_python_dir(
        'get',
        path=f'{path}/app/source/views/{name.lower()}/methods'
    )

    make_python_dir(
        'patch',
        path=f'{path}/app/source/views/{name.lower()}/methods'
    )

    make_python_dir(
        'post',
        path=f'{path}/app/source/views/{name.lower()}/methods'
    )

    make_file(
        'schemas.py',
        path=f'{path}/app/source/views/{name.lower()}',
        text=make_schema(name)
    )

    make_file(
        'document.py',
        path=f'{path}/app/source/views/{name.lower()}/methods/get',
        text=make_document_for_get_method(name)
    )

    make_file(
        'document.py',
        path=f'{path}/app/source/views/{name.lower()}/methods/post',
        text=make_document_for_post_and_patch_method(name)
    )

    make_file(
        'document.py',
        path=f'{path}/app/source/views/{name.lower()}/methods/patch',
        text=make_document_for_post_and_patch_method(name)
    )

    make_file(
        'document.py',
        path=f'{path}/app/source/views/{name.lower()}/methods/delete',
        text=make_document_for_delete_method(name)
    )

    append_to_file(
        '__init__.py',
        path=f'{path}/app/source/views/{name.lower()}/methods',
        text=f"\nname = '{name.capitalize()}'\n"
    )

    make_file(
        'handler.py',
        path=f'{path}/app/source/views/{name.lower()}/methods/get',
        text=make_handler_for_get_method(name)
    )

    make_file(
        'handler.py',
        path=f'{path}/app/source/views/{name.lower()}/methods/patch',
        text=make_handler_for_patch_method(name)
    )

    make_file(
        'handler.py',
        path=f'{path}/app/source/views/{name.lower()}/methods/delete',
        text=make_handler_for_delete_method(name)
    )

    make_file(
        'handler.py',
        path=f'{path}/app/source/views/{name.lower()}/methods/post',
        text=make_handler_for_post_method(name)
    )

    append_to_file(
        '__init__.py',
        path=f'{path}/app/source/views/{name.lower()}',
        text=f"from app.source.views.{name.lower()}.methods.get import GetView\n"
             f"from app.source.views.{name.lower()}.methods.patch import UpdateView\n"
             f"from app.source.views.{name.lower()}.methods.post import CreateView\n"
             f"from app.source.views.{name.lower()}.methods.delete import DeleteView\n"
             "\n"
             "\n"
             f"class {name.capitalize()}HandlerView(\n"
             "    GetView,\n"
             "    UpdateView,\n"
             "    CreateView,\n"
             "    DeleteView\n"
             "):\n"
             "    pass\n"
    )

    append_import_to_file(
        'routes.py',
        path=path + '/app/source',
        importing=f'from app.source.views.{name.lower()} import {name.capitalize()}HandlerView'
    )

    append_text_to_file_after_specified_string(
        'routes.py',
        specify_string='def setup_routes(app):',
        path=path + '/app/source',
        text=f'app.router.add_view("/{name.lower()}", {name.capitalize()}HandlerView)'
    )

    append_to_file(
        "__init__.py",
        path=f'{path}/app/source/views/{name.lower()}/methods/delete',
        text=f"from app.source.views.{name.lower()}.methods.delete.handler import Handler\n"
             "\n"
             "\n"
             "class DeleteView(\n"
             "    Handler\n"
             "):\n"
             "    pass\n"
    )

    append_to_file(
        "__init__.py",
        path=f'{path}/app/source/views/{name.lower()}/methods/get',
        text=f"from app.source.views.{name.lower()}.methods.get.handler import Handler\n"
             "\n"
             "\n"
             "class GetView(\n"
             "    Handler\n"
             "):\n"
             "    pass\n"
    )

    append_to_file(
        "__init__.py",
        path=f'{path}/app/source/views/{name.lower()}/methods/patch',
        text=f"from app.source.views.{name.lower()}.methods.patch.handler import Handler\n"
             "\n"
             "\n"
             "class UpdateView(\n"
             "    Handler\n"
             "):\n"
             "    pass\n"
    )

    append_to_file(
        "__init__.py",
        path=f'{path}/app/source/views/{name.lower()}/methods/post',
        text=f"from app.source.views.{name.lower()}.methods.post.handler import Handler\n"
             "\n"
             "\n"
             "class CreateView(\n"
             "    Handler\n"
             "):\n"
             "    pass\n"
    )

    append_model(name, path)

    append_text_to_file_after_specified_string(
        'accessor.py',
        path=path + '/app/store/database',
        specify_string='def __init__(self):',
        text=f"from app.source.models import {name.capitalize()}"
    )

    append_text_to_file_after_specified_string(
        'accessor.py',
        path=path + '/app/store/database',
        specify_string=f"from app.source.models import {name.capitalize()}",
        text=f'self.{name.lower()} = {name.capitalize()}'
    )


def remove_object(name: str, path: str):
    """
        Make object with CRUD methods of rest api.
        :param path:
        :param name: name of object.
        :return:
        """
    drop_python_dir(
        name.lower(),
        path=path + '/app/source/views'
    )

    remove_text_from_file(
        'routes.py',
        path=path + '/app/source',
        text=f'from app.source.views.{name.lower()} import {name.capitalize()}HandlerView'
    )

    remove_text_from_file(
        'routes.py',
        path=path + '/app/source',
        text=f'app.router.add_view("/{name.lower()}", {name.capitalize()}HandlerView)'
    )

    remove_model(name, path)

    remove_text_from_file(
        'accessor.py',
        path=path + '/app/store/database',
        text=f"from app.source.models import {name.capitalize()}"
    )

    remove_text_from_file(
        'accessor.py',
        path=path + '/app/store/database',
        text=f'self.{name.lower()} = {name.capitalize()}'
    )