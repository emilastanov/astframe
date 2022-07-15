CONFIG = "common:\n" \
         "  port: 8080 # порт, на котором будет работать сервер\n" \
         "postgres:\n" \
         "  database_url: postgres://admin:admin@localhost # адрес базы данных\n" \
         "  require_ssl: false # стоит ли шифровать соединение с базой\n"

SETTINGS = "import pathlib\n" \
           "import yaml\n" \
           "\n" \
           "BASE_DIR = pathlib.Path(__file__).parent.parent\n" \
           "config_path = BASE_DIR / 'config' / 'config.yaml'\n" \
           "\n" \
           "\n" \
           "def get_config(path):\n" \
           "    with open(path) as f:\n" \
           "        parsed_config = yaml.safe_load(f)\n" \
           "        return parsed_config\n" \
           "\n" \
           "\n" \
           "config = get_config(config_path)\n"
