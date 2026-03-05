# Умовні конструкції

# user = int(input("Enter some: "))
# hasBobCar = True

# if user >= 5 or not hasBobCar:
#     print("Hello")
#     num2 = int(input("Enter number: "))
#     if num2 <= 10:
#         print("Number < 10")
# elif user == 8:
#     print("Number is 8!")
# elif (user < 3 and user > -3) or not hasBobCar:
#     print("Between 3 and -3")
# else:
#     print("Incorrect number")


#Самостійна робота

num1 = float(input("Enter the number 1 : "))
operation = input("Enter +, -, *, / ")
num2 = float(input("Enter the number 2 : "))

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Error: division by zero'
else:
    result = 'Error: incorrect operation'
print(f'Result operation: {result}')