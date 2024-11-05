dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 2, 'b': 3, 'c': 4}

result = {}

for key in dict1:
    result[key] = dict1[key] + dict2[key]

print(result)