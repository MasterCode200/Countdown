
def countdown(x):
    for number in range(x,-1,-2):
        if (number==0):
            print("It is Over")
        else:
                print(number)

y=int(input("From which number do you want to countdown from? "))
countdown(y)