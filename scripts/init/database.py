ACCESSOR = "from aiohttp import web\n" \
             "\n" \
             "\n" \
             "class PostgresAccessor:\n" \
             "    def __init__(self):\n" \
             "        # Make model in /app/source/models.py and append it here.\n" \
             "        # from app.source.models import Model\n" \
             "\n" \
             "        # self.model_name = Model\n" \
             "\n" \
             "        self.db = None\n" \
             "\n" \
             "    def setup(self, application: web.Application) -> None:\n" \
             "        application.on_startup.append(self._on_connect)\n" \
             "        application.on_cleanup.append(self._on_disconnect)\n" \
             "\n" \
             "    async def _on_connect(self, application: web.Application):\n" \
             "        from app.store.database.models import db\n" \
             "\n" \
             "        self.config = application['config']['postgres']\n" \
             "        await db.set_bind(self.config['database_url'])\n" \
             "        self.db = db\n" \
             "\n" \
             "    async def _on_disconnect(self, _) -> None:\n" \
             "        if self.db is not None:\n" \
             "            await self.db.pop_bind().close()\n" \
             "\n"
