a = {'age': '18', 'name': 'Pavel', 'country': 'Minsk'}
b = {value: key for key, value in a.items()}
print(b)
