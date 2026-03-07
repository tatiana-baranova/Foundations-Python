# Функції
# def test(word):
#     print(word, "!", sep="")
#     # pass

# def add(x, y, additional=0):
#     result = "Res:", str(x + y + additional)
#     test(result)
#     return x + y + additional

# def mul(x, y, *args):
#     print(x, y, args)

# def mul(*args):
#     for i in args:
#         i *= 2
#         print(f"Element: {i}")

# user1 = int(input('Enter num 1: '))
# user2 = int(input('Enter num 2: '))
# data = add(user1, user2, 10)
# print(data)
# mul(5, 6, 8, True, "Some")

# def nums(**kwargs):
#     for key, value in kwargs.items():
#         print(f'Element {value}, key: {key}')

# nums(x=10, additional="10", y=True)

# Практичний приклад
data1 = dict(x=5, v=8, z=7, a=1, d=20)
# minElement = 1000
# for k, v in data1.items():
#     if v < minElement:
#         minElement = v
# print(f"Min Element: {minElement}")

data2 = dict(x=50, v=8, z=7, a=-10, d=20)
# minElement = 1000
# for k, v in data2.items():
#     if v < minElement:
#         minElement = v
# print(f"Min Element: {minElement}")


# def minimal(nums):
#     minElement = 1000
#     for v in nums.values():
#         if v < minElement:
#             minElement = v
#     # print(f"Min Element: {minElement}")
#     return minElement

# min1 = minimal(data1)
# min2 = minimal(data2)

# if min1 < min2: print(min1)
# else: print(min2)

# Lambda 
# mul = lambda x, y: x * y
# print(mul(5,7))
# print(mul(3,5))


# Самостійна робота

def multiply(x, v):
    print(x * v)
multiply(5, 3)

def greet(name, age):
    return f"Hello {name}! You {age}."

result_greet = greet("Anna", 25)
print(result_greet)