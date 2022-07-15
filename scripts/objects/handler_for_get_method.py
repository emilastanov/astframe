def make_handler_for_get_method(name):
    return "from aiohttp import web\n" \
           "\n" \
           "from app.middlewares.objects import get_object_by_id, get_objects\n" \
           "from app.middlewares.errors import UnknownObject, NoId\n" \
           "from app.source.data_formats import query_data, UNKNOWN_OBJECT\n" \
           f"from app.source.views.{name.lower()}.methods.get.document import swagger_extension\n" \
           f"from app.source.views.{name.lower()}.methods import name\n" \
           "\n" \
           "__all__ = ('Handler', )\n" \
           "\n" \
           "\n" \
           "class Handler(web.View):\n" \
           "\n" \
           "    @swagger_extension\n" \
           "    async def get(self):\n" \
           "\n" \
           "        try:\n" \
           "            _object = await get_object_by_id(self.request, name)\n" \
           "            response = query_data(_object)\n" \
           "\n" \
           "        except UnknownObject:\n" \
           "            response = UNKNOWN_OBJECT\n" \
           "\n" \
           "        except NoId:\n" \
           "            objects = await get_objects(self.request, name)\n" \
           "            response = query_data(**objects)\n" \
           "\n" \
           "        return web.json_response(**response)\n"
