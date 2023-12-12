import datetime
import re

from requests import get
from bs4 import BeautifulSoup

WEATHER_DOMAIN = "http://www.chelpogoda.ru"


class RealWeatherParser:
    resource = WEATHER_DOMAIN + "/weather/actual:{}/"

    def parse(self, date: datetime.date):
        soup = BeautifulSoup(get(self.resource.format(date)).text, "lxml")

        table = soup.find("form", {"name": "show_actual_weather"}).find_next_sibling("table")
        if table is None:
            return None

        weather_row = table.find_all("tr")[2]
        weather_col = weather_row.find_all("td")[1]
        weather_text = weather_col.find("li").text
        temperature = re.findall(r"-?\d+", weather_text)[0]

        return temperature


class WeatherForecastParser:
    resource = WEATHER_DOMAIN + "/weather"
    all_months = ["январь", "февраль", "март", "апрель", "май", "июнь",
                  "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

    def parse(self):
        soup = BeautifulSoup(get(self.resource).text, "lxml")

        res = []

        table = soup.find("table", string=re.compile("Прогноз погоды по Челябинску")).find_next_sibling("table")
        weather_rows = table.find_all("tr")
        for row in weather_rows[2::2]:
            cols = row.find_all_next("td")
            date_text = cols[0].find_next("br").next_sibling.text
            temperatures = re.findall(r"-?\d+", row.find_all_next("td")[4].text)
            temperatures = list(map(int, temperatures))

            avg_temperature = sum(temperatures) // len(temperatures)

            today = datetime.date.today()

            day = int(re.findall(r"\d+", date_text)[0])
            month = self.all_months.index(re.findall(r"[а-яА-Я]+", date_text)[0].lower()) + 1
            year = today.year + (1 if month < today.month else 0)

            res.append((datetime.date(year, month, day), avg_temperature))

        return res
