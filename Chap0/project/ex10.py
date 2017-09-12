# Task 9 Guess data Phase II
import random

def Num():
    num = random.sample(range(0,10), 4)
    while num[0] == 0:
        num = random.sample(range(0,10), 4)
    return num
#number = Num()
#print ("The random num is %s" % number)

def guess():

    guesses = input("> ")

    if guesses.isdigit() and len(guesses) == 4:
        get_num = []
        for x in guesses:
            get_num.append(int(x))
        return get_num
    else:
        print("Hi man, please give 4 digits!")

#b = guess()
#print(b)

def comp(number, answer):
    a = c = 0
    for x in range(4):
        if number[x] == answer [x]:
            a+=1
    for y in answer:
        if y in number:
            c+=1
    b = c - a # it is very important, it will remove the number which both are correct in position and value.
    return a, b

def play():

    try:
        print("it starts")
        number = Num()
        times = 9
#        print ("The random num is %s" % number)
        while times >= 0:
            answer = guess()
            print("You still have %d times" % times)
            times -= 1
            A,B = comp(number,answer)
            print ("%dA%dB" % (A,B))
            if A == 4:
                print("Congrats,you are right!")
                exit(0)

        if times < 0:
            print("We are sorry, you have no chance!")
            print ("The random num is %s" % number)
    except:
        print ("Di...Di...Di")

play()
