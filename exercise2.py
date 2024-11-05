num = int(input())
lst = []
lst.append(num)

while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = 3 * num + 1
    lst.append(num)
a = ""
for n in lst:
    a += str(n) + ","
a = a[0:-1]
print(a)

