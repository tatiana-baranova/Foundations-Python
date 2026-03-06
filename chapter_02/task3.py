# Кортежи - tuple

# data = (5, 4, 6, True, [4, 2])
# print(data[1::2])
# print(data.count(5))
# print(len(data))

# word = tuple("Some")
# print(word)

# #Множини - set
# data2 = {5, 2, 5, 6, 3}
# data2.add(33)
# data2.remove(6)
# data2.pop()  # видалення останього елементу
# print(data2)


# word2 = set("Hello world")
# print(word2)

# Незміна множина

# data3 = frozenset({3, 0, 6, 4, 5, 9, 8})
# word3 = frozenset("Hello world")
# print(word3)
# print(data3)

# Словники
# user = {'name': 'Alex', 'age': 25}
# print(user['name'])

# user1 = {'name': 'Alex', 'age': 25, 5: 4, True: (4, 6), (4, 1): 23}
# user1[(4, 1)] = False
# user1.popitem()
# user1.pop('age')
# #user1.clear()
# user1['new'] = 45
# data = user1.copy()
# print(user1)
# print(data)


# Великий об'єкт
# users = {
#     'user1':{"name": "Alex", "age": 23, "data": [5, 3, 2, 3], "bio": "Some text", "address": {"city": "New York", "street": "some street"}},
#     'user2':{"name": "Den", "age": 23, "data": [5, 3, 2, 3], "bio": "Some text", "address": {"city": "New York", "street": "some street"}},
#     'user3':{"name": "Alisa", "age": 23, "data": [5, 3, 2, 3], "bio": "Some text", "address": {"city": "New York", "street": "some street"}},
#     'user4':{"name": "Bob", "age": 23, "data": [5, 3, 2, 3], "bio": "Some text", "address": {"city": "New York", "street": "some street"}},
#     'user5':{"name": "Gon", "age": 23, "data": [5, 3, 2, 3], "bio": "Some text", "address": {"city": "New York", "street": "some street"}},
# }
# print(users['user3']['name'])
# print(users['user3']['address']['city'])

#Самостійна робота

colors = ('red', 'green', 'blue')
fruits_set = {'apple', 'banana', 'orange'}
ages = {'Anna': 25, 'Ivan': 30, 'Maria': 22}

print(colors[1])
colors += ('yellow',)
print(colors)
print(fruits_set)
ages['Ivan'] = 32
print(list(ages.keys()))
fruits_set.remove('orange')
print(ages.items())