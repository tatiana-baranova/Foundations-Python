#Обробка файлів

try:
    num = int(input('Enter num: '))#file1.txt
    # f = open(f'data/file{num}.txt', 'r')
    # print(f.read())
    # f.close()

    with open(f'data/file{num}.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
except ValueError:
    print('Enter the number please')
finally:
    print('Finish')
