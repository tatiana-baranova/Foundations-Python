str_list = [["some", "special"], ["text", "for", "you"], ["-", 50]]
result = []
for el in str_list:
    for item in el:
        result.append(str(item))

print(' '.join(result))