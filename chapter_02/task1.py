# Списки данних

data = [5, 2.3, True, "Hello", [4, 7]]
# data[2] = False
numbers = [9, 5, 2]
data.append("info")
data.extend(numbers)
data.insert(1, [4, 5, 6])

data.remove('info')
data.pop()

numbers.sort()
numbers.reverse()
print(numbers)

# data.clear()
print(data.count(5))
print(len(data))

