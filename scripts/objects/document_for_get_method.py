def make_document_for_get_method(name: str):
    return "from aiohttp_apispec import docs\n" \
           "\n" \
           f"from app.source.views.{name.lower()}.methods import name\n" \
           "from app.source.views.schemas import response_schema\n" \
           f"from app.source.views.{name.lower()}.schemas import {name.capitalize()}\n" \
           "\n" \
           "\n" \
           "def swagger_extension(method):\n" \
           "    @docs(\n" \
           "        tags=[name],\n" \
           "        summary='Read',\n" \
           f"        description='''Method for getting list of {name.lower()}.''',\n" \
           "        # parameters=[{\n" \
           "        #     'in': 'header',\n" \
           "        #     'name': 'Authorization',\n" \
           "        #     'description': 'Access token.',\n" \
           "        #     'schema': {'type': 'string'},\n" \
           "        #     'required': 'true'\n" \
           "        # }],\n" \
           "        responses={\n" \
           "            200: {\n" \
           f"                'schema': response_schema({name.capitalize()}, many=True),\n" \
           "                'description': 'List.'\n" \
           "            }\n" \
           "        }\n" \
           "    )\n" \
           "    def extension(*args, **kwargs):\n" \
           "        return method(*args, **kwargs)\n" \
           "\n" \
           "    return extension\n"
