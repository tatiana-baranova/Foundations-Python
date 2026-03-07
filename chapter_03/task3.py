# Генератори
def generator(lis):
    for i in lis:
        yield i

val = generator([5, 2, 5, 6])
print(next(val))
print('Hello')
print(next(val))
print(next(val))
print(next(val))