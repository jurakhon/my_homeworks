original_dict = {'apple': 10, 'banana': 5, 'cherry': 15}

sorted_dict = dict(sorted(original_dict.items(), key=lambda item: item[1]))

print(sorted_dict)