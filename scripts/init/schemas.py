SCHEMAS = "from marshmallow import Schema, fields\n" \
             "\n" \
             "\n" \
             "class Error(Schema):\n" \
             "    status = fields.Str()\n" \
             "    error = fields.Str()\n" \
             "\n" \
             "\n" \
             "class Identifier(Schema):\n" \
             "    id = fields.Int()\n" \
             "\n" \
             "\n" \
             "class Status(Schema):\n" \
             "    status = fields.Str()\n" \
             "\n" \
             "\n" \
             "def response_schema(schema, many=False):\n" \
             "    class Response(Schema):\n" \
             "        status = fields.Str()\n" \
             "        data = fields.Nested(schema, many=many)\n" \
             "\n" \
             "    Response.__name__ = f'{schema.__name__}ResponseSchema'\n" \
             "    return Response\n"
