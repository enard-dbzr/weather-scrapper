import logging

from flask import Flask, render_template
from sqlalchemy import select
from sqlalchemy.sql.expression import func

from models import db_session
from models.weather import Weather

app = Flask(__name__)


@app.route("/")
def index():
    with db_session.create_session() as db:
        uniq_ids = select(func.min(Weather.id)).group_by(Weather.date, Weather.forecasted_temp)
        weather_data = db.scalars(select(Weather).where(Weather.id.in_(uniq_ids)))

        return render_template("index.html", weather_data=weather_data)
