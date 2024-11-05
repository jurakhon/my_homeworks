num = input("Enter numbers and press enter: ")
num = [int(x) for x in num.split()]

print(f"sort1: {sorted(num)}")
print(f"sort2: {sorted(num, reverse=True)}")
