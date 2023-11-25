import json
import logging

from flask import Flask, render_template
from sqlalchemy import select
from sqlalchemy.sql.expression import func

from models import db_session
from models.weather import Weather

app = Flask(__name__)


@app.route("/")
def index():
    with (db_session.create_session() as db):
        uniq_ids = select(func.min(Weather.id)).group_by(Weather.date, Weather.forecasted_temp)
        weathers = db.scalars(select(Weather)
                              .where(Weather.id.in_(uniq_ids))
                              .order_by(Weather.date.desc(), Weather.id.desc())).all()

    real = [{"date": w.date.isoformat(), "temp": w.real_temp} for w in weathers if w.real_temp is not None][::-1]
    forecasted = [{"date": w.date.isoformat(), "temp": w.forecasted_temp} for w in weathers][::-1]

    distances = [abs(w.real_temp - w.forecasted_temp)
                 if w.real_temp is not None else None for w in weathers]

    return render_template("index.html",
                           weather_data=zip(weathers, distances),
                           real_timeline=json.dumps(real),
                           forecasted_timeline=json.dumps(forecasted))
