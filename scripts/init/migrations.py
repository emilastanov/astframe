MIGRATIONS = "from logging.config import fileConfig\n" \
             "\n" \
             "from alembic import context\n" \
             "from sqlalchemy import create_engine\n" \
             "\n" \
             "from app.settings import config as app_config\n" \
             "from app.store.database.accessor import PostgresAccessor\n" \
             "from app.store.database.models import db\n" \
             "\n" \
             "config = context.config\n" \
             "fileConfig(config.config_file_name)\n" \
             "target_metadata = db\n" \
             "\n" \
             "\n" \
             "def run_migrations_online():\n" \
             "    # For Alembic available only models which import at the moment of migration.\n" \
             "    # PostgresAccessor do initialize and import required models, for generating migrations " \
             "automatic\n" \
             "    PostgresAccessor()\n" \
             "    connectable = create_engine(app_config['postgres']['database_url'])\n" \
             "    with connectable.connect() as connection:\n" \
             "        context.configure(connection=connection, target_metadata=target_metadata)\n" \
             "        with context.begin_transaction():\n" \
             "            context.run_migrations()\n" \
             "\n" \
             "\n" \
             "run_migrations_online()\n"
