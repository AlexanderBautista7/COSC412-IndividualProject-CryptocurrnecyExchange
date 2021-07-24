from flask import Flask, render_template, request, flash, redirect, jsonify
import config, csv
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
app.secret_key = b'M8PXq8Y7WZ3VvZpXMWWCXHufvVGwt3rHxSEm75W11anGinkJolo1ZwAhbynWP0Zn'
client = Client(config.API_KEY, config.API_SECRET, tld = 'us')

@app.route('/Home', methods = ['GET', 'POST'])
def Home():
    return render_template('Home.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Info')
def Info():
    return render_template('Info.html')

@app.route('/ContactUs')
def ContactUs():
    return render_template('ContactUs.html')

@app.route('/LogIn')
def LogIn():
    return render_template('LogIn.html')

@app.route("/GigaExchange")
def GigaExchange():

    title = 'GigaExchange'

    account = client.get_account()

    balances = account['balances']

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('GigaExchange.html', title = title, my_balances = balances, symbols = symbols)

@app.route('/buy', methods = ['POST'])
def buy():
    print(request.form)
    try:
        order = client.create_test_order(symbol = request.form['symbol'],
            side = SIDE_BUY,
            type = ORDER_TYPE_MARKET,
            quantity = request.form['quantity'])
    except Exception as e:
            flash(e.message, "error")
        
    return redirect('/')
    
@app.route('/sell', methods = ['POST'] )
def sell():
    print(request.form)
    try:
        order = client.create_test_order(symbol = request.form['symbol'],
            side = SIDE_SELL,
            type = ORDER_TYPE_MARKET,
            quantity = request.form['quantity'])
    except Exception as e:
            flash(e.message, "error")


@app.route('/settings')
def setting():
    return "settings"

@app.route('/history')
def history():
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jul, 2021", "22 July, 2021")

    processed_candlesticks = []
    
    for data in candlesticks:
        candlestick = { 
            "time": data[0] / 1000 , 
            "open": data[1], 
            "high": data[2], 
            "low": data[3], 
            "close": data[4]
            }

        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)

@app.route('/LogIn', methods = ['POST', 'GET'])
def LogIn():
    return render_template("LogIn.html")

@app.route('/<usr>')
def user(usr):
    return f"<h1>{usr}</h1>"