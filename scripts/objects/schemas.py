def make_schema(name: str):
    return "from marshmallow import Schema, fields\n" \
           "from app.middlewares.objects import get_object_attributes\n" \
           f"from app.source.views.{name.lower()}.methods import name\n" \
           "\n" \
           "\n" \
           "def make_attributes_of_schema():\n" \
           "    attributes = get_object_attributes(name)\n" \
           "\n" \
           "    attr = {}\n" \
           "    for field in attributes:\n" \
           "\n" \
           "        if attributes[field]['type'] == 'INTEGER':\n" \
           "            attr[field] = fields.Int()\n" \
           "        elif attributes[field]['type'] == 'DATETIME':\n" \
           "            attr[field] = fields.DateTime()\n" \
           "        elif attributes[field]['type'] == 'DATE':\n" \
           "            attr[field] = fields.Date()\n" \
           "        else:\n" \
           "            attr[field] = fields.Str()\n" \
           "\n" \
           "    return attr\n" \
           "\n" \
           "\n" \
           f"{name.capitalize()} = type(name, (Schema,), make_attributes_of_schema())\n"
