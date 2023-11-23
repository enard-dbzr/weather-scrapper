import os

from models.db_session import global_init

if __name__ == "__main__":
    global_init(f"postgresql+psycopg2://"
                f"{os.getenv('POSTGRES_USER')}:"
                f"{os.getenv('POSTGRES_PASSWORD')}@"
                f"{os.getenv('POSTGRES_HOST')}:"
                f"{os.getenv('POSTGRES_PORT')}/"
                f"{os.getenv('POSTGRES_USER')}")
