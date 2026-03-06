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
#     if el == 'l': print('Found')

for i in range(10, 20):
    if i % 2 == 0: continue
    print(f"Element: {i}")
    if i == 15: break