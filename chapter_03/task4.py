# Робота з файлами
# f = open('data/file.txt', 'a')
# user_data = input('Enter data: ')
# f.write(user_data + '\n')

f = open('data/file.txt', 'r')
# print(f.read(20))
for line in f:
    print(line, end='')
f.close()

