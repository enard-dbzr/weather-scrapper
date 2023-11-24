import datetime
from typing import Optional

from sqlalchemy.orm import mapped_column, Mapped

from .db_session import SqlAlchemyBase


class Weather(SqlAlchemyBase):
    __tablename__ = "weather"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[datetime.date]
    real_temp: Mapped[Optional[int]]
    forecasted_temp: Mapped[int]

    def __repr__(self):
        return (f"Weather(id={self.id}, date={self.date}, "
                f"real={self.real_temp}, forecasted={self.forecasted_temp})")

