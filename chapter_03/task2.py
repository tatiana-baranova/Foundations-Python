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