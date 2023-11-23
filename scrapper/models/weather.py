import datetime

from sqlalchemy.orm import mapped_column, Mapped

from .db_session import SqlAlchemyBase


class RealWeather(SqlAlchemyBase):
    __tablename__ = "weather"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    day_temperature: Mapped[int]
    night_temperature: Mapped[int]
    req_time: Mapped[datetime.datetime]
