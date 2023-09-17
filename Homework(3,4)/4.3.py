def items(b):
    dict = {}

    for i in b:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    return dict


list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]
result = items(list)

for key, value in result.items():
    print(f"Число {key} встречается {value} раз")