def make_handler_for_patch_method(name):
    return "from aiohttp import web\n" \
           "\n" \
           "from app.middlewares.errors import UnknownObject, IncorrectBody\n" \
           "from app.middlewares.objects.response import make_response\n" \
           f"from app.source.views.{name.lower()}.methods import name\n" \
           f"from app.source.views.{name.lower()}" \
           f".methods.patch.document import swagger_extension\n" \
           "from app.middlewares.objects import update_object\n" \
           "\n" \
           "__all__ = ('Handler', )\n" \
           "\n" \
           "\n" \
           "from app.source.data_formats import (\n" \
           "    INCORRECT_REQUEST_BODY,\n" \
           "    UNKNOWN_OBJECT,\n" \
           "    data_updated\n" \
           ")\n" \
           "\n" \
           "\n" \
           "class Handler(web.View):\n" \
           "\n" \
           "    @swagger_extension\n" \
           "    async def patch(self):\n" \
           "        try:\n" \
           "            _object = await update_object(self.request, name)\n" \
           "\n" \
           "            response = data_updated(await make_response(name, _object))\n" \
           "\n" \
           "        except IncorrectBody:\n" \
           "            response = INCORRECT_REQUEST_BODY\n" \
           "\n" \
           "        except UnknownObject:\n" \
           "            response = UNKNOWN_OBJECT\n" \
           "\n" \
           "        return web.json_response(**response)\n"
