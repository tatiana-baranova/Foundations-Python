# Цикли в мові Python

# i = 1000
# while i > 10:
#     print(f"Element: {i}")
#     i /= 5

# isRunning = True
# while isRunning: 
#     user = int(input('Enter the number 0: '))
#     if user == 0:
#         isRunning = False
# print("Finish!")

# for i in range(6, 11):
#     print(f"Element: {i}")


# word = "Hello"
# for el in word:
#     if el == '!': 
#         print('Found')
#         break
# else:
#     print("Not found")

# for i in range(10, 20):
#     if i % 2 == 0: continue
#     print(f"Element: {i}")
#     if i == 15: break

# # Практичні приклади
# data = {5, 7, True, 7,  "Word"}
# user = {"name": "Alisa", "age": 25, (6, 7): True, False: 7.7}
# for el in user.items():
#     print (f"element: {el[0]}. Value: {el[1]}")

# for key, el in user.items():
#     print(f"Element: {key}, value: {el}")


# user_data = []

# number = int(input("Enter number: "))
# for i in range(number):
#     el = input("Enter value: ")
#     user_data.append(el)
# print(user_data)

# maxElement = user_data[0]
# for i in user_data: 
#     if i > maxElement: 
#         maxElement = i
# print(f"Max element: {maxElement}")