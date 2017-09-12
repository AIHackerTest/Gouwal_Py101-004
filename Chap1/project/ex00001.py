# coding: utf-8

def generate_dict(file):
    weather_dict = {}


    with open(file) as f:
        for line in f:
            # 字符串分割，先用strip()干掉'\n'，再用split(',')，调整成 --> ['北京', '晴']格式
            # data = line.strip().split(',')
            # weather_dict[data[0]] = data[1]

            return weather_dict



def history_print(list):
    if len(list) == 0:
        print("暂无查询记录\n")
    else:
        print("您的查询记录为：")
        print("----城市--------天气----")


        for i in range(len(list)):
            print("%6s    %6s" % (list[i][0], list[i][1]))
        print('\n')
    return 0


def main():
    file = '../resource/weather_info.txt'
    dict = generate_dict(file)


    print("本程序用来查询各城市天气\n"
           "输入『help』查看帮助\n"
           "输入『history』查看查询历史纪录\n"
           "输入『exit』退出程序\n")


    history = []


    while True:
        user = input("请输入城市名称或指令：").strip()


        if user in dict:
                    # 历史纪录中删除重复项，以第一次查询为准
             # 否则还要动态调整history[]的顺序，太tmd麻烦了......
             if [user, dict[user]] not in history:
                 history.append([user, dict[user]])


             print(user, " 的天气为：", dict[user], '\n')


        elif user == 'help' or user == 'h':
            print("帮助文档懒得写，自己琢磨吧\n")


        elif user == 'history' or user == 'his':
            history_print(history)


        elif user == 'exit' or user == 'exi' or user == 'ex' or user == 'e':
             break


        else:
             print("城市名称无法识别！！\n")




if __name__ == "__main__":
    main()
