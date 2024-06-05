# The Calculator App

# Task 1

# Arithmetic operations with parameters for two numbers

num1 = 10
num2 = 2

def addition(num1, num2):
    return num1 + num2
total = addition(10,2)
print(total)

def subtraction(num1, num2):
    return num1 - num2
total = subtraction(10,2)
print(total)

def multiplication(num1, num2):
    return num1 * num2
total = multiplication(10,2)
print(total)

def division(num1, num2):
    return num1 / num2
total = division(10,2)
print(total)

Task 2

# User input to receive numbers and operation choice with associated functions

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
operation = str(input(" Enter the operation of choice"))

if operation == "addition":
    # print("{} + {}=".format(num1, num2))
    print(addition(num1, num2))

if operation == "subtraction":
    # print("{} - {}=".format(num1, num2))
    print(subtraction(num1, num2))

if operation == "multiplication":
    # print("{} * {}=".format(num1, num2))
    print(multiplication(num1,num2))

if operation == "division":
    # print("{} / {}=".format(num1, num2))
    print(division(num1, num2))

# The Shopping List Maker

# # Task 1

shopping_list = ["milk",'eggs','bread']
print("Current Shopping List", shopping_list)
# new_item = input("item")

# input1 = (input("Would you like to add or remove an item to the list?"))
# input2 = (input("What item would you like to add?"))
# input3 = (input("What item would you like remove from the list?"))
# item = (input())

def menu():
    while True:
        input1 = input("Would you like to add, remove or view an item to the list?")
        if input1 == "add":
            input1 = input("What item would you like to add?")
            shopping_list.append(input1)
        elif input1 == "remove":
            input1 = input("What item would you like remove from the list?")
            shopping_list.remove(input1)
        elif input1 == "view":
            print(shopping_list)
            break

def add():
    input1 = input("What item would you like to add?:")
    shopping_list.append(input1)

def remove():
    input1 = input("What item would you like remove from the list?:")
    shopping_list.append(input1)

def view():
    input1 = input("Updated shopping List")
    print(shopping_list)

menu()
    
