#-*-coding:utf-8 -*-
from flask import render_template
from flask import Flask
from flask import request
app = Flask(__name__)
import requests
import json

history_list = [] #list
url = 'https://api.seniverse.com/v3/weather/now.json'

# API 抓取信息，并设置location为待输入变量
def fetchWeather(location):
    result = requests.get(url, params={
        'key': 'efl6u8iobdjg9jxd',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
        }, timeout=1)
    result = result.json() # Very import very import, if no this syntax, there is a erro called "subscriptable"
    weather = result['results'][0]['now']['text'] #因为result是由一个Dir+list+Dir组成, for [0],becaues it's a list which only have 1 element
    temp = result['results'][0]['now']['temperature']
    updated_time = result['results'][0]['last_update']
    updated_time = updated_time.split('T')[0]

    weather_str = f'{location}天气:{weather},气温:{temp}℃\n更新时间:{updated_time}.\n'
    return weather_str

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_request')
def process_request():

    try:
        request.args.get('query') == "查询"
        city = request.args.get('city')
        weather_str = fetchWeather(city)
        history_list.append(weather_str)
        return render_template("query.html", weather_str=weather_str)
    except:
        if request.args.get('history') == "历史":
            return render_template("history.html", history_list=history_list)
        if request.args.get('help') == "帮助":
            return render_template('help.html')

        else:
            return render_template("error.html",city=city)

if __name__ == "__main__":
    app.run(debug=True)
