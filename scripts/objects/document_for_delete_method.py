def make_document_for_delete_method(name):
    return "from aiohttp_apispec import docs, request_schema\n" \
           "from marshmallow import Schema, fields\n" \
           "\n" \
           "from app.source.views.schemas import (\n" \
           "    Status,\n" \
           "    Identifier\n" \
           ")\n" \
           f"from app.source.views.{name.lower()}.methods import name\n" \
           "\n" \
           "\n" \
           "def swagger_extension(method):\n" \
           "    @docs(\n" \
           "        tags=[name],\n" \
           "        summary='Delete',\n" \
           f"        description='''Method for deleting {name.lower()}.''',\n" \
           "        # parameters=[{\n" \
           "        #     'in': 'header',\n" \
           "        #     'name': 'Authorization',\n" \
           "        #     'description': 'Access token.',\n" \
           "        #     'schema': {'type': 'string'},\n" \
           "        #     'required': 'true'\n" \
           "        # }],\n" \
           "        responses={\n" \
           "            202: {\n" \
           "                'schema': Status,\n" \
           "                'description': 'Статус процесса удаления.'\n" \
           "            }\n" \
           "        }\n" \
           "    )\n" \
           "    @request_schema(Identifier())\n" \
           "    def extension(*args, **kwargs):\n" \
           "        return method(*args, **kwargs)\n" \
           "\n" \
           "    return extension\n"
