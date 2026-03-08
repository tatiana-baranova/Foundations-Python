#Обробка файлів

try:
    num = int(input('Enter num: '))#file1.txt
    f = open(f'data/file{num}.txt', 'r')
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File not found")
except ValueError:
    print('Enter the number please')
finally:
    print('Finish')
