import time

# Декоратор функцій
# def auth(func):
#     def wrapper():
#         isAuth = True
#         if isAuth == True:
#             func()
#         else:
#             print("Вам потрібно авторизуватися")
#     return wrapper

# def test(func):
#     def wrapper():
#         print("Text before function")
#         func()
#         print("Text after function")
#     return wrapper

# @test
# def show():
#     print("Show function")

# def about():
#     print("About function")

# @auth
# @test
# def profile():
#     print("Profile function")

# @auth
# def reg():
#     print("Reg function")

# # show()
# profile()


# def multiply(x, y):
#     return x * y


# def double_result(func):
#     def wrapper(x, y):
#         result = func(x, y)
#         return result * 2
#     return wrapper

# @double_result
# def multiply(x, y):
#     return x * y

# result = multiply(6, 7)
# print(f"Результат множення з подвоєням: {result}")


# def log_function(func):
#     def wrapper(*args, **kwargs):
#         print("Function started")
#         result = func(*args, **kwargs)
#         print("Function finished")
#         return result
#     return wrapper

# @log_function
# def say_hello():
#     print("Hello")

# say_hello()

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         execution_time = end - start
#         print(f"Функція виконувалась: {execution_time:.2f} секунд")
#         return result
#     return wrapper

# @timer
# def slow_function():
#     time.sleep(2)
#     print("Функція виконана")

# slow_function()