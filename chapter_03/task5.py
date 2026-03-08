# Обробник винятків
isUserInput = False
while not isUserInput:
    try:
        num = int(input("Enter the num: "))
        isUserInput = True
        print(num)
    except ValueError:
        print("Enter the number please")



        