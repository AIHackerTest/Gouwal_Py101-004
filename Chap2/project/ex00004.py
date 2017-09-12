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
    return result.json() # ()一定要有，否则返回的只是一个方法。

#print(result)
#{"results":[{"location":{"id":"WX4FBXXFKE4F","name":"北京","country":"CN","path":"北京,北京,中国","timezone":"Asia/Shang
#hai","timezone_offset":"+08:00"},"now":{"text":"阴","code":"9","temperature":"24"},"last_update":"2017-08-26T22:50:00+08
#:00"}]}
def get_weather_info():
    try:
        location = city
        result = fetchWeather(location)
        weather = result['results'][0]['now']['text'] #因为result是由一个Dir+list+Dir组成, for [0],becaues it's a list which only have 1 element
        temp = result['results'][0]['now']['temperature']
        updated_time = result['results'][0]['last_update']
        updated_time = updated_time.split('T')[0]

        weather_str = f'{location}天气:{weather},气温:{temp}℃\n更新时间:{updated_time}.\n'
        print(weather_str)

#        print('{}:\nWeather is :{}'.format(location, weather))
#        print('Temperature is :{} ℃'.format(temp))
#        print('Updated time is :{}'.format(updated_time))
#        history[location] = 'Weather is :' + weather,'Temperature is :' + temp + '℃','Updated time is :' + updated_time
        history_list.append(weather_str) # impressive

    except:
        print("sorry, the city you input is inexistent, please input again") # it means any irre erro above with call this syntax
        get_help()


def get_help():
    print ('''
    Input the city name, search fot city weater;
    Input Help or H or h, get more help;
    Input history, for more previous search info;
    Input exit,quit,q or Q, for stoppint the program
    ''')

def get_history():
#    for key, value in history.items():
#        print('{}: \n{}'.format(key, value))
    for info in history_list: #very good, when take history_list as a list not dictionary
        print(info)

while True:
    city = input("Please input the city name: ")
    if city == "help" or city == "Help" or city == 'h' or city == 'H':
        get_help()
    elif city == 'history':
        get_history()
    elif city == 'exit' or city == 'q' or city =='quit' or city == 'Q':
        exit(0)
    else:
        get_weather_info()
