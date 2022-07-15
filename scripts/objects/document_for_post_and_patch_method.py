def make_document_for_post_and_patch_method(name):
    return "from aiohttp_apispec import docs, request_schema\n" \
           "\n" \
           f"from app.source.views.{name.lower()}.methods import name\n" \
           f"from app.source.views.{name.lower()}.schemas import {name.capitalize()}\n" \
           "from app.source.views.schemas import Error\n" \
           "\n" \
           "\n" \
           "def swagger_extension(method):\n" \
           "    @docs(\n" \
           "        tags=[name],\n" \
           "        summary='Create',\n" \
           f"        description='''Method for creating {name.lower()}.''',\n" \
           "        # parameters=[{\n" \
           "        #     'in': 'header',\n" \
           "        #     'name': 'Authorization',\n" \
           "        #     'description': 'Access token.',\n" \
           "        #     'schema': {'type': 'string'},\n" \
           "        #     'required': 'true'\n" \
           "        # }],\n" \
           "        responses={\n" \
           "            200: {\n" \
           f"                'schema': {name.capitalize()},\n" \
           "                'description': 'Data.'\n" \
           "            },\n" \
           "            400: {\n" \
           "                'schema': Error,\n" \
           "                'description': 'Already exist.'\n" \
           "            }\n" \
           "        }\n" \
           "    )\n" \
           f"    @request_schema({name.capitalize()}())\n" \
           "    def extension(*args, **kwargs):\n" \
           "        return method(*args, **kwargs)\n" \
           "\n" \
           "    return extension\n" \
           "\n"
