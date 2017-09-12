# Advanced Task
from random import randint

data = randint(0,21)

guess = int(input("> "))

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
    guess = int(input("> "))

    if guess > data:
        print ("What you guess is bigger")
    elif guess < data:
        print ("What you guess is smaller")
    else:
        print ("Excellent, you are right")
if guess != data:
        print ("Sorry, you are so....")
        print ("And the answer is %d" % data)
