import os
def addition (num1, num2):
    return int(num1) + int(num2)
def subtraction (num1, num2):
    return int(num1) - int(num2)
def multiplication (num1, num2):
    return int(num1) * int(num2)
def division (num1, num2):
    return int(num1) / int(num2)



while True:
    exit = None
    os.system("cls")
    math = input ("(1)Addition  (2)Subtraction  (3)Multiplication  (4)Division  (Enter)Exit\n")
    os.system("cls")
    if int(math) == 1:
        number1 = input ("First number: ")
        os.system("cls")
        number2 = input ("First number: " + number1 + "\nSecond number: ")
        os.system("cls")
        answer = addition (number1, number2)
        print ("First number: " + number1 + "\nSecond number: " + number2 + "\nAnswer: " + str(answer))
        exit = input ("\nExit(1)  Go back(2)\n")
        if int(exit) == 1:
            break
        elif int(exit) == 2:
            continue
    elif int(math) == 2:
        number1 = input ("First number: ")
        os.system("cls")
        number2 = input ("First number: " + number1 + "\nSecond number: ")
        os.system("cls")
        answer = subtraction (number1, number2)
        print ("First number: " + number1 + "\nSecond number: " + number2 + "\nAnswer: " + str(answer))
        exit = input ("\nExit(1)  Go back(2)\n")
        if int(exit) == 1:
            break
        elif int(exit) == 2:
            continue
    elif int(math) == 3:
        number1 = input ("First number: ")
        os.system("cls")
        number2 = input ("First number: " + number1 + "\nSecond number: ")
        os.system("cls")
        answer = multiplication (number1, number2)
        print ("First number: " + number1 + "\nSecond number: " + number2 + "\nAnswer: " + str(answer))
        exit = input ("\nExit(1)  Go back(2)\n")
        if int(exit) == 1:
            break
        elif int(exit) == 2:
            continue
    elif int(math) == 4:
        number1 = input ("First number: ")
        os.system("cls")
        number2 = input ("First number: " + number1 + "\nSecond number: ")
        os.system("cls")
        answer = division (number1, number2)
        print ("First number: " + number1 + "\nSecond number: " + number2 + "\nAnswer: " + str(answer))
        exit = input ("\nExit(1)  Go back(2)\n")
        if int(exit) == 1:
            break
        elif int(exit) == 2:
            continue
    else:
        os.system("cls")
        input ("That is not a viable option")
        continue