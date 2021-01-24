import os
import csv
import talib
import pandas
import yfinance as yf
from flask import Flask, escape, request, render_template
from patterns import candlestick_patterns

app = Flask(__name__)


@app.route('/scanner')
def scanner():
    pattern = request.args.get('pattern', False)
    fet = request.args.get('fet')
    stocks = {}

    with open('data/symbols.csv') as f:
        for row in csv.reader(f):
            stocks[row[0]] = {'company': row[1]}

    if pattern:
        for filename in os.listdir('data/stocks'):
            df = pandas.read_csv('data/stocks/{}'.format(filename))
            pattern_function = getattr(talib, pattern)
            symbol = filename.split('.')[0]

            try:
                results = pattern_function(
                    df['Open'], df['High'], df['Low'], df['Close'])
                last = results.tail(1).values[0]

                if last > 0:
                    stocks[symbol][pattern] = 'bullish'
                elif last < 0:
                    stocks[symbol][pattern] = 'bearish'
                else:
                    stocks[symbol][pattern] = None
            except Exception as e:
                print('Failed on File: ', filename, e)
    elif fet:
        fetch_data()

    return render_template('scanner.html', candlestick_patterns=candlestick_patterns, stocks=stocks, pattern=pattern, fet=fet, active='scanner')


@app.route('/about')
def about():
    return render_template('about.html', active="about")


@app.route('/patterns')
def patterns():
    return render_template('patterns.html', active="pattern")


@app.route('/fetch_data')
def fetch_data():
    with open('data/symbols.csv') as f:
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[0]
            # print(symbol)
            data = yf.download(
                # date format: yyyy-mm-dd
                symbol + '.NS', start="2017-01-01", end="2020-12-24")
            data.to_csv('data/stocks/{}.csv'.format(symbol))

    return {
        "code": "success"
    }


@app.route('/')
def index():
    return render_template('index.html', active='home')
