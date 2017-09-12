#-*-coding:utf-8 -*-
with open("C:/Users/CNNEZHA2/mystuff/py104/py101-004/chap1/project/weather_info.txt", 'r') as f:
    content = f.readlines()
    weather_info = {}


    for line in content:
        line = line.strip('\n').split(',')
        weather_info[line[0]] = line[1].strip("''")

def find_weather():
    histories = ''
    while True:
        order = input("请输入指令或您要查询的城市名>")
        if order in weather_info.keys():
            weather = weather_info[order]
            history = '%s : %s\n' % (order, weather)
            histories += history
            print("%s的天气状况为：%s " % (order,weather))

        elif order == 'help':
                print("""
 - 输入城市名，查询该城市的天气；
 - 输入help，获取帮助文档；
 - 输入history，获取查询历史；
 - 输入quit，退出天气查询系统；
                         """)
        elif order == 'history' and len(histories) > 0:
            print(histories)
        elif order == 'history' and histories == '':
            print ("暂无记录")

        elif order == 'quit':
            return
        else:
            print("查询不到相关城市")

find_weather()
