import datetime
import logging

from sqlalchemy import select

import parsers
from models import db_session
from models.weather import Weather


class Connector:
    def __init__(self):
        self.real_parser = parsers.RealWeatherParser()
        self.forecasted_paser = parsers.WeatherForecastParser()

    def tick(self):
        with db_session.create_session() as db:
            for date, temperature in self.forecasted_paser.parse():
                weather = Weather(date=date, forecasted_temp=temperature)

                logging.debug(f"Received forecast: {weather}")

                db.add(weather)

            db.commit()

            to_get = db.scalars(select(Weather).where(Weather.date <= datetime.date.today(),
                                                      Weather.real_temp == None))

            for weather in to_get:
                temp = self.real_parser.parse(weather.date)
                if temp is not None:
                    weather.real_temp = temp
                logging.debug(f"Updated weather: {weather}")

            db.commit()
