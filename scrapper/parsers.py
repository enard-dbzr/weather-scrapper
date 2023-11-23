import datetime
import re

from requests import get
from bs4 import BeautifulSoup


class RealWeatherParser:
    link = "http://www.chelpogoda.ru/weather/actual:{}/"

    def parse(self, date: datetime.date):
        soup = BeautifulSoup(get(self.link.format(date)).text, "lxml")

        table = soup.find("form", {"name": "show_actual_weather"}).find_next_sibling("table")
        weather_row = table.find_all("tr")[2]
        weather_col = weather_row.find_all("td")[1]
        weather_text = weather_col.find("li").text
        temperature = re.findall(r"-?\d+", weather_text)[0]

        return temperature


class WeatherForecast:
    link = ""
