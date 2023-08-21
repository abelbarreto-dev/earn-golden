from dotenv import load_dotenv

from os import system

from src.utils.db_urls import get_mysql_url


def set_alembic_ini(deps: bool = load_dotenv()) -> None:
    init_alembic = "alembic init alembic"

    system(init_alembic)

    database_url = get_mysql_url()
    to_replace_database_url = f"sqlalchemy.url = {database_url}"
    file = "alembic.ini"

    with open(file, "r") as alembic:
        data = alembic.readlines()

        data[62] = to_replace_database_url

    with open(file, "w") as alembic:
        alembic.writelines(data)


def set_base_metadata_env_py() -> None:
    file = "alembic/env.py"
    package = "src.database.data"
    classname = "Base"

    with open(file, "r") as alembic:
        data = alembic.readlines()

    import_base = f"from {package} import {classname}\n"
    base_metadata = f"{classname}.metadata"

    if import_base not in data[6: 9]:
        data[6] = f"\n{import_base}\n"

    data[22] = data[22].replace("None", base_metadata)

    with open(file, "w") as alembic:
        alembic.writelines(data)


if __name__ == '__main__':
    set_alembic_ini()
    set_base_metadata_env_py()
