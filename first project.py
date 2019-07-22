def main():
    #print("Hello World")
    #variable = input("what is your name")
    #print(variable)

    four()

def two():
    x=10
    print(x)

def three():
    num = input("what is your number")
    print (num)
    if num > 10:
        print("greater than 10")
    if num < 10:
        print("less than 10")
    if num == 10:
        print("equal to 10")

def four():
    number = input("what's your number")
    print (number)
    if number %2 == 1:
        print("your number is odd")
    if number %2 == 0:
        print("your number is even")


if __name__ == "__main__":
    main()

