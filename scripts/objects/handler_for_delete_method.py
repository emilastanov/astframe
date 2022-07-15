def make_handler_for_delete_method(name: str):
    return "from aiohttp import web\n" \
           "\n" \
           "from app.middlewares.errors import UnknownObject, IncorrectBody\n" \
           f"from app.source.views.{name.lower()}.methods import name\n" \
           f"from app.source.views.{name.lower()}.methods.delete.document import swagger_extension\n" \
           "from app.middlewares.objects import delete_object\n" \
           "from app.source.data_formats import (\n" \
           "    INCORRECT_REQUEST_BODY,\n" \
           "    UNKNOWN_OBJECT,\n" \
           "    DELETED\n" \
           ")\n" \
           "\n" \
           "__all__ = ('Handler',)\n" \
           "\n" \
           "\n" \
           "class Handler(web.View):\n" \
           "\n" \
           "    @swagger_extension\n" \
           "    async def delete(self):\n" \
           "\n" \
           "        try:\n" \
           "            await delete_object(self.request, name, ['id'])\n" \
           "            response = DELETED\n" \
           "\n" \
           "        except UnknownObject:\n" \
           "            response = UNKNOWN_OBJECT\n" \
           "\n" \
           "        except IncorrectBody:\n" \
           "            response = INCORRECT_REQUEST_BODY\n" \
           "\n" \
           "        return web.json_response(**response)\n"
