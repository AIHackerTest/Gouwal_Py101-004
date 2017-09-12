# Tase5 Previous 19
def cheese_and_cracker(cheese_count, boxes_of_crackers):
    print("You have %d chesses!" % cheese_count) #when I use %d, it always have a warning"TypeError: %d format: a number is required, not str"
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

print ("We can just give the function numbers directly")

#cheese_and_cracker(input("We have cheese "), input("We have crackers "))
cheese_and_cracker(int(input("We have cheese ")), int(input("We have crackers "))) # resovled
