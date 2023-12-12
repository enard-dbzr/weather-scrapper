import logging
import os
import time

import sqlalchemy.exc

from database import db_session
from web import app

db_connection_str = (f"postgresql+psycopg2://"
                     f"{os.getenv('POSTGRES_USER')}:"
                     f"{os.getenv('POSTGRES_PASSWORD')}@"
                     f"{os.getenv('POSTGRES_HOST')}:"
                     f"{os.getenv('POSTGRES_PORT')}/"
                     f"{os.getenv('POSTGRES_USER')}")

logging.basicConfig(format="[%(levelname)s]: %(asctime)s - %(name)s - %(message)s",
                    level=os.getenv("DEBUG_LEVEL", "INFO"))


def init_app():
    while True:
        try:
            db_session.global_init(db_connection_str)
            break
        except sqlalchemy.exc.OperationalError:
            logging.error("Failed to connect db")
            time.sleep(10)

    return app


if __name__ == "__main__":
    init_app().run()
