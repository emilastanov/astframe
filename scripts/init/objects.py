INIT_FILE = "from app.middlewares.objects.create import handler as create_object\n" \
            "from app.middlewares.objects.update import handler as update_object\n" \
            "from app.middlewares.objects.delete import handler as delete_object\n" \
            "from app.middlewares.objects.attributes import *\n" \
            "from app.middlewares.objects.query import *\n"

CREATE = "from app.middlewares.objects.attributes import get_object_attributes\n" \
         "from app.middlewares.objects.request import get_request_json_body\n" \
         "\n" \
         "\n" \
         "async def handler(request, model, validator=lambda res: res):\n" \
         "    attributes = get_object_attributes(model)\n" \
         "    request_data = validator(await get_request_json_body(request, attributes))\n" \
         "\n" \
         "    return await getattr(request.app['db'], model).create(**request_data)\n"

DELETE = "from app.middlewares.errors import UnknownObject\n" \
         "from app.middlewares.objects.request import get_request_json_body\n" \
         "from app.source import models\n" \
         "\n" \
         "\n" \
         "async def handler(request, model, attributes):\n" \
         "    request_data = await get_request_json_body(" \
         "request, attributes, get_object_id=True, use_require_fields=False" \
         ")\n" \
         "    model = getattr(models, model)\n" \
         "\n" \
         "    _object = await model.get(request_data['id'])\n" \
         "\n" \
         "    if _object:\n" \
         "        return await _object.delete()\n" \
         "    else:\n" \
         "        raise UnknownObject\n"

QUERY = "from app.middlewares.errors import UnknownObject, NoId\n" \
        "from app.middlewares.objects.response import make_response\n" \
        "from app.source import models\n" \
        "\n" \
        "\n" \
        "async def get_object_by_id(request, model_name):\n" \
        "    object_id = request.query.get('id')\n" \
        "\n" \
        "    model = getattr(models, model_name)\n" \
        "\n" \
        "    if object_id:\n" \
        "        _object = await model.get(int(object_id))\n" \
        "    else:\n" \
        "        raise NoId\n" \
        "\n" \
        "    if _object:\n" \
        "        return await make_response(model_name, _object)\n" \
        "    else:\n" \
        "        raise UnknownObject\n" \
        "\n" \
        "\n" \
        "async def get_objects(request, model_name):\n" \
        "    limit = request.query.get('limit') or 100\n" \
        "    offset = request.query.get('offset') or 0\n" \
        "\n" \
        "    model = getattr(models, model_name)\n" \
        "\n" \
        "    data = await model.__table__.select().limit(limit).offset(offset).gino.all()\n" \
        "    count = await models.db.func.count(model.id).gino.scalar()\n" \
        "\n" \
        "    objects = [await make_response(model_name, _object) for _object in data]\n" \
        "\n" \
        "    return {\n" \
        "        'data': objects,\n" \
        "        'limit': limit,\n" \
        "        'offset': offset,\n" \
        "        'count': count\n" \
        "    }\n"

REQUEST = "from json import JSONDecodeError\n" \
         "\n" \
         "from app.middlewares.errors import IncorrectBody\n" \
         "\n" \
         "\n" \
         "async def get_request_json_body(request, attributes, get_object_id=False, use_require_fields=True):\n" \
         "    try:\n" \
         "        request_data = await request.json()\n" \
         "\n" \
         "        object_data = {}\n" \
         "        for attr in attributes:\n" \
         "            if attr == 'id':\n" \
         "                if get_object_id:\n" \
         "                    object_data[attr] = request_data[attr]\n" \
         "            elif attributes[attr]['required'] and use_require_fields:\n" \
         "                object_data[attr] = request_data[attr]\n" \
         "            else:\n" \
         "                object_data[attr] = request_data.get(attr)\n" \
         "\n" \
         "        return object_data\n" \
         "\n" \
         "    except JSONDecodeError:\n" \
         "        raise IncorrectBody\n" \
         "    except KeyError:\n" \
         "        raise IncorrectBody\n"

RESPONSE = "from app.middlewares.objects.attributes import get_object_attributes\n" \
             "\n" \
             "\n" \
             "async def make_response(model, _object):\n" \
             "    attributes = get_object_attributes(model)\n" \
             "    response_data = {}\n" \
             "    for attr in attributes:\n" \
             "        if attributes[attr]['type'] in ('DATE', 'DATETIME', 'UUID'):\n" \
             "            response_data[attr] = str(getattr(_object, attr))\n" \
             "        else:\n" \
             "            response_data[attr] = getattr(_object, attr)\n" \
             "    return response_data\n"

UPDATE = "from app.middlewares.objects.attributes import get_object_attributes\n" \
         "from app.middlewares.objects.request import get_request_json_body\n" \
         "from app.middlewares.errors import UnknownObject\n" \
         "from app.source import models\n" \
         "\n" \
         "\n" \
         "async def handler(request, model):\n" \
         "    attributes = get_object_attributes(model)\n" \
         "\n" \
         "    request_data = await get_request_json_body(" \
         "request, attributes, get_object_id=True, use_require_fields=False" \
         ")\n" \
         "\n" \
         "    update_data = {}\n" \
         "    for field in request_data:\n" \
         "        if request_data[field]:\n" \
         "            update_data[field] = request_data[field]\n" \
         "\n" \
         "    _object = await getattr(models, model).get(update_data.pop('id'))\n" \
         "\n" \
         "    if _object and update_data:\n" \
         "        await _object.update(**update_data).apply()\n" \
         "    elif not _object:\n" \
         "        raise UnknownObject\n" \
         "\n" \
         "    return _object\n"

ATTRIBUTES = "from app.source import models\n" \
             "\n" \
             "\n" \
             "def get_object_attributes(model):\n" \
             "    model = getattr(models, model)\n" \
             "    attributes = {}\n" \
             "    for attribute in [\n" \
             "                         key\n" \
             "                         for key in model.__dict__.keys()\n" \
             "                         if '__' not in key\n" \
             "                     ][:-1]:\n" \
             "        attributes[attribute] = {\n" \
             "            'required': not model\n" \
             "                .__dict__[attribute]\n" \
             "                .__dict__['column'].nullable,\n" \
             "            'type': str(model\n" \
             "                .__dict__[attribute]\n" \
             "                .__dict__['column']\n" \
             "                .__dict__['type']).upper()\n" \
             "        }\n" \
             "    return attributes\n"
