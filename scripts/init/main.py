MAIN = "from aiohttp import web\n" \
             "from aiohttp_apispec import setup_aiohttp_apispec\n" \
             "\n" \
             "from app.settings import config\n" \
             "from app.store.database.accessor import PostgresAccessor\n" \
             "\n" \
             "\n" \
             "def setup_accessors(application):\n" \
             "    application['db'] = PostgresAccessor()\n" \
             "    application['db'].setup(application)\n" \
             "\n" \
             "\n" \
             "def setup_config(application):\n" \
             "    application['config'] = config\n" \
             "\n" \
             "\n" \
             "def setup_routes(application):\n" \
             "    from app.source.routes import setup_routes as imported_routes\n" \
             "    imported_routes(application)\n" \
             "\n" \
             "\n" \
             "def setup_documentation(application):\n" \
             "    setup_aiohttp_apispec(\n" \
             "        app=application,\n" \
             "        title='{title}',\n" \
             "        version='v1',\n" \
             "        url='/api/docs/swagger.json',\n" \
             "        swagger_path='/' # Documentation root\n" \
             "    )\n" \
             "\n" \
             "\n" \
             "def setup_app(application):\n" \
             "    setup_documentation(application)\n" \
             "    setup_config(application)\n" \
             "    setup_routes(application)\n" \
             "    setup_accessors(application)\n" \
             "\n" \
             "\n" \
             "app = web.Application()\n" \
             "\n" \
             "if __name__ == '__main__':\n" \
             "    setup_app(app)\n" \
             "    try:\n" \
             "        web.run_app(app, port=config['common']['port'])\n" \
             "    except OSError:\n" \
             "        print('You must to connect database in the file /config/config.yaml.')\n"
