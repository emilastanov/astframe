
def make_requirements() -> None:
    """
    Make requirements.
    """
    file = open("requirements.txt", "w")
    file.write("aiohttp==3.7.3\n"
               "aiohttp-apispec==2.2.3\n"
               "aiosmtplib==1.1.6\n"
               "alembic==1.7.7\n"
               "apispec==3.3.2\n"
               "async-timeout==3.0.1\n"
               "asyncpg==0.25.0\n"
               "attrs==21.4.0\n"
               "certifi==2021.10.8\n"
               "gino==1.0.1\n"
               "marshmallow==3.15.0\n"
               "multidict==6.0.2\n"
               "packaging==21.3\n"
               "psycopg2-binary==2.9.3\n"
               "pyparsing==3.0.8\n"
               "PyYAML==6.0\n"
               "requests==2.27.1\n"
               "SQLAlchemy==1.3.24\n"
               "typing_extensions==4.1.1\n"
               "urllib3==1.26.9\n"
               "webargs==5.5.3\n"
               "httpx==0.22.0\n")
    file.close()
    print(f'astframe: requirements.txt created.')
