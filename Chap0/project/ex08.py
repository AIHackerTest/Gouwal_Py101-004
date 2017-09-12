# Advanced Task
from random import randint

data = randint(0,21)

initial = 0

initial = input("> ")

if "0" in initial or "1" in initial:
    guess = int(initial)
else:
    print ("Man, learn to type a number.")

#guess = int(input("> "))
guess = int(initial)
if guess > data:
    print ("What you guess is bigger")
elif guess < data:
    print ("What you guess is smaller")
else:
    print ("Excellent, you are right")


i = 0
while guess != data and i < 9:
    times = 9 - i
    print ("You only have %d times" % times)
    i+=1
#    guess = int(input("> "))
    initial = input("> ")
    if "0" in initial: #or "1" in initial:
        guess = input(initial)
    else:
        print ("Man, learn to type a number.")

    if guess > data:
        print ("What you guess is bigger")
    elif guess < data:
        print ("What you guess is smaller")
    else:
        print ("Excellent, you are right")
if guess != data:
        print ("Sorry, you are so....")
        print ("And the answer is %d" % data)
