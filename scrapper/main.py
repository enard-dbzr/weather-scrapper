import time
import os
import logging

import schedule
import sqlalchemy.exc

from connector import Connector
from database.db_session import global_init

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
            time.sleep(5)
            global_init(db_connection_str)
            break
        except (sqlalchemy.exc.OperationalError, sqlalchemy.exc.IntegrityError):
            logging.error("Failed to connect db")

    con = Connector()

    schedule.every(int(os.getenv("INTERVAL", 24))).hours.do(con.tick)

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
