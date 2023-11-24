import time
import os
import logging

import schedule
import sqlalchemy.exc

from connector import Connector
from models.db_session import global_init

logging.basicConfig(format="[%(levelname)s]: %(asctime)s - %(name)s - %(message)s",
                    level=os.getenv("DEBUG_LEVEL", "INFO"))

db_connection_str = (f"postgresql+psycopg2://"
                     f"{os.getenv('POSTGRES_USER')}:"
                     f"{os.getenv('POSTGRES_PASSWORD')}@"
                     f"{os.getenv('POSTGRES_HOST')}:"
                     f"{os.getenv('POSTGRES_PORT')}/"
                     f"{os.getenv('POSTGRES_USER')}")

if __name__ == "__main__":
    while True:
        try:
            global_init(db_connection_str)
            break
        except sqlalchemy.exc.OperationalError:
            logging.error("Failed to connect db")
            time.sleep(10)

    con = Connector()

    schedule.every(os.getenv("INTERVAL", 24)).seconds.do(con.tick)

    con.tick()

    while True:
        try:
            schedule.run_pending()
            time.sleep(10)
        except KeyboardInterrupt:
            break
        except Exception:
            logging.exception("Got exception on main")
            time.sleep(60)
