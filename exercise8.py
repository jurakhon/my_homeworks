a = input("enter your sentence: ").split()

text = ""
for i in a:
    text += "".join(i+" ")
print(text)

words = text.lower().split()

my_dict = {}

for i in words:
    if i.lower() in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

print(my_dict)