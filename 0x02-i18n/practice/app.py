#!/usr/bin/env python3

from flask import Flask, render_template, request
from datetime import date, datetime
from flask_babel import numbers, dates, Babel, format_date, gettext
app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)


@babel.localeselector
def get_locale():
    return 'es'
    # return request.


@app.route('/')
def index():
    name = gettext('Anthony')
    us_num = numbers.format_decimal(12345, locale='en_US')
    se_num = numbers.format_decimal(12345, locale='sv_SE')
    ge_num = numbers.format_decimal(12345, locale='de_DE')
    d = date(2023, 8, 29)
    us_date = dates.format_date(d, locale='en_US')
    se_date = format_date(d)
    ge_date = dates.format_date(d, locale='de_DE')
    dt = datetime(2023, 8, 29, 10, 49)
    us_format = dates.format_datetime(dt, locale='en_US')
    results = {'us_num': us_num, 'se_num': se_num, 'de_num': ge_num,
               'us_date': us_date, 'se_date': se_date,
               'ge_date': ge_date, 'us_format': us_format}
    return render_template('index.html', results=results, name=name)


if __name__ == '__main__':
    app.run(debug=True)
