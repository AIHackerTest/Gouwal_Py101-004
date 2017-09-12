# Tast06 Previous exercise 21
def add(a, b):
    print (("ADDING %d + %d") % (a,b))
    return a + b

def subtract(a, b):
    print ("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print ("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print ("DIVIDING %d / %d" % (a, b))
    return a / b

print ("Let's do some math with just functions!")

age = add(int(input("age= ")), int(input("math scores= ")))
print ("Your final Age scores = %d" % age)
height = subtract(int(input("Pure height = ")), int(input("Leg length = ")))
print ("Your final height scores = %d" % height)
weight = multiply (int(input("Pure weight = ")), int(input("Foot height = ")))
print ("Your final weight scores = %d" % weight)
iq = float(divide (age*height, weight))
# iq = divide (height*weight, weight)
print("*" * 50)
print ("And Your IQ IS = %s " % iq)
print("*" * 50)
