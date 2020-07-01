#******************************************************************************
#Simple Calculater :addition subraction, multiplication and division
#Author: Wilder J Gomez
#Description: This simple calculator will do simple Arithmitic,using "While loop", "Functions", "If Statement"
#Date 6/26/2020
#*******************************************************************************/
user_input = int(input("please enter 1 for CALCULATOR: "))

while user_input == 1:
    num1 = int(input("please enter the num1: "))
    num2 = int(input("please enter the num 2: "))
    more_cal = int(input("for sum press 1:\nfor subtraction press 2: \nfor multiplication press 3:\nfor division press 4: "))


    ##########################function###########################
    def addition(num1, num2):
        sum1 = num1 + num2
        print("-----------------------")
        print("|    the sum is: ", sum1, "   |")
        print("-----------------------")

    ##########################function###########################
    def subtraction(num1, num2):
        sub1 = num1 - num2
        print("-----------------------")
        print("|    the subtraction is: ", sub1, "   |")
        print("-----------------------")

    ##########################function###########################
    def product(num1, num2):
        multi = num1 * num2
        print("-----------------------")
        print("|    the product is: ", multi, "   |")
        print("-----------------------")

    ##########################function###########################
    def div(num1, num2):
        division = num1 / num2
        print("-----------------------")
        print("|    the division is: ", division, "   |")
        print("-----------------------")

    # -----------------------MENU--------------------------------
    if more_cal == 1:
        addition(num1, num2)
    elif more_cal == 2:
        subtraction(num1, num2)
    elif more_cal == 3:
        product(num1, num2)
    elif more_cal == 4:
        div(num1, num2)
    else:

        print(" *  * Invalid input * *")

