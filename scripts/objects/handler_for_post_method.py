def make_handler_for_post_method(name: str):
    return "from aiohttp import web\n" \
           "import asyncpg.exceptions\n" \
           "\n" \
           "from app.middlewares.errors import IncorrectBody\n" \
           "from app.middlewares.objects.response import make_response\n" \
           "from app.middlewares.objects import create_object\n" \
           f"from app.source.views.{name.lower()}.methods import name\n" \
           "from app.source.data_formats import (\n" \
           "    INCORRECT_REQUEST_BODY,\n" \
           "    OBJECT_ALREADY_EXIST,\n" \
           "    data_created\n" \
           ")\n" \
           f"from app.source.views.{name.lower()}.methods.post.document import swagger_extension\n" \
           "\n" \
           "__all__ = ('Handler',)\n" \
           "\n" \
           "\n" \
           "class Handler(web.View):\n" \
           "\n" \
           "    @swagger_extension\n" \
           "    async def post(self):\n" \
           "\n" \
           "        try:\n" \
           "            _object = await create_object(self.request, name.lower())\n" \
           "\n" \
           "            response = data_created(await make_response(name, _object))\n" \
           "\n" \
           "        except asyncpg.exceptions.UniqueViolationError:\n" \
           "            response = OBJECT_ALREADY_EXIST\n" \
           "\n" \
           "        except IncorrectBody:\n" \
           "            response = INCORRECT_REQUEST_BODY\n" \
           "\n" \
           "        return web.json_response(**response)\n"
