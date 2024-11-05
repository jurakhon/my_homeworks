import math

n = 100000

result = []
for num in range(10, n):
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in str(num))
    if num == sum_of_factorials:
        result.append(num)
print(result)
