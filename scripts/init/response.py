SUCCESS = "from aiohttp import web\n" \
          "\n" \
          "DELETED = {\n" \
          "    'data': {\n" \
          "        'status': 'deleted'\n" \
          "    },\n" \
          "    'status': web.HTTPAccepted.status_code\n" \
          "}\n" \
          "\n" \
          "\n" \
          "SUCCESS = {\n" \
          "    'data': {\n" \
          "        'status': 'ok'\n" \
          "    },\n" \
          "    'status': web.HTTPOk.status_code\n" \
          "}\n" \
          "\n" \
          "\n" \
          "def query_data(data, **additional_args):\n" \
          "    response = {\n" \
          "        'data': {\n" \
          "            'status': 'ok',\n" \
          "            'data': data\n" \
          "        },\n" \
          "        'status': web.HTTPOk.status_code\n" \
          "    }\n" \
          "    if additional_args:\n" \
          "        for key in additional_args:\n" \
          "            response['data'][key] = additional_args[key]\n" \
          "    return response\n" \
          "\n" \
          "\n" \
          "def data_updated(data):\n" \
          "    return {\n" \
          "        'data': {\n" \
          "            'status': 'ok',\n" \
          "            'data': data\n" \
          "        },\n" \
          "        'status': web.HTTPAccepted.status_code\n" \
          "    }\n" \
          "\n" \
          "\n" \
          "def data_created(data):\n" \
          "    return {\n" \
          "        'data': {\n" \
          "            'status': 'ok',\n" \
          "            'data': data\n" \
          "        },\n" \
          "        'status': web.HTTPCreated.status_code\n" \
          "    }\n"

FAILED = "from aiohttp import web\n" \
         "\n" \
         "INCORRECT_REQUEST_BODY = {\n" \
         "    'data': {\n" \
         "        'status': 'error',\n" \
         "        'data': {\n" \
         "            'error': 'Incorrect request body.'\n" \
         "        }\n" \
         "    },\n" \
         "    'status': web.HTTPBadRequest.status_code\n" \
         "}\n" \
         "\n" \
         "UNKNOWN_OBJECT = {\n" \
         "    'data': {\n" \
         "        'status': 'error',\n" \
         "        'data': {\n" \
         "            'error': 'Unknown object.'\n" \
         "        }\n" \
         "    },\n" \
         "    'status': web.HTTPNotFound.status_code\n" \
         "}\n" \
         "\n" \
         "OBJECT_DOES_NOT_EXIST = {\n" \
         "    'data': {\n" \
         "        'status': 'error',\n" \
         "        'data': {\n" \
         "            'error': 'Object does not exits.'\n" \
         "        }\n" \
         "    },\n" \
         "    'status': web.HTTPNotFound.status_code\n" \
         "}\n" \
         "\n" \
         "PERMISSION_DENIED = {\n" \
         "    'data': {\n" \
         "        'status': 'error',\n" \
         "        'data': {\n" \
         "            'error': 'Permission denied.'\n" \
         "        }\n" \
         "    },\n" \
         "    'status': web.HTTPForbidden.status_code\n" \
         "}\n" \
         "\n" \
         "OBJECT_ALREADY_EXIST = {\n" \
         "    'data': {\n" \
         "        'status': 'error',\n" \
         "        'data': {\n" \
         "            'error': 'Object already exist.'\n" \
         "        }\n" \
         "    },\n" \
         "    'status': web.HTTPBadRequest.status_code\n" \
         "}\n"
