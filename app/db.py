from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.settings import Settings, get_settings


def initialize_database(app: FastAPI, settings: Settings = get_settings()) -> None:
    register_tortoise(
        app=app,
        db_url=settings.db_url,
        modules={
            "models": [
                "app.models.tortoise.vacancy",
                "app.models.tortoise.employer",
            ]
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )


# TODO: update when db initializing needed
# from tortoise import Tortoise, connections, run_async
# from tortoise.utils import get_schema_sql
#
#
# async def generate_first_schema():
#     await Tortoise.init(
#         db_url="sqlite://db.sqlite3",
#         modules={
#             "models": [
#                 "models.tortoise.vacancy",
#                 "models.tortoise.employer",
#             ]
#         }
#     )
#     await Tortoise.generate_schemas()
#     sql = get_schema_sql(client=connections.get("default"), safe=True)
#     print(sql)
#     await Tortoise.close_connections()
#
#
# if __name__ == "__main__":
#     run_async(generate_first_schema())
