n = int(input("enter a number: "))
lst = []

for i in range(1, n + 1):
    div_sum = 0
    for j in range(1, i):
        if i % j == 0:
            div_sum += j
    if div_sum == i:
        lst.append(i)
print(lst)