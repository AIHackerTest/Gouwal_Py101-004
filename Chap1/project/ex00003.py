
weather = {}
history = {}

with open('C:\\Users\\CNNEZHA2\\mystuff\\Py104\\Py101-004\\Chap1\\project\\weather_info.txt', 'r', encoding = 'utf-8') as f:
    for line in f.readlines():
        key = line.split(',')[0]
        value = line.split(',')[1]
        weather[key] = value # Create the dictionary of weather information

def get_help():
    print ('''
    Input the city name, search fot city weater;
    Input Help or H or h, get more help;
    Input history, for more previous search info;
    Input exit, for stoppint the program
    ''')

def get_history():
    for key, value in history.items():
        print('{}:{}'.format(key, value))

def get_weather_info():
    try:
        print('{} the weather is :{}'.format(city, weather[city]))
        history[city] = weather[city]
    except:
        print("sorry, the city you input is inexistent, please input again")
        get_help()

while True:
    city = input("Please input the city name: ")
    if city == "help" or city == "Help" or city == 'h' or city == 'H':
        get_help()
    elif city == 'history':
        get_history()
    elif city == 'exit':
        exit(0)
    else:
        get_weather_info()
