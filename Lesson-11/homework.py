# 1-masala

total = 0
while True:
    n = int(input("Enter a number: "))
    if n == 0:
        break
    if n > 0:
        total += n
print("Sum:", total)

# 2-masala

A = int(input("Enter A: "))
B = int(input("Enter B: "))
sum_ab = 0
while A <= B:
    sum_ab += A
    A += 1
print("Sum from A to B:", sum_ab)

# 3-masala

numbers = []
while True:
    n = input("Enter a number: ")
    if n == "":
        break
    numbers.append(int(n))
print("List:", numbers)

# 4-masala

x = [1, 2, 3, 14, 5, 6, 6, 7]
max_elem = x[0]
i = 1
while i < len(x):
    if x[i] > max_elem:
        max_elem = x[i]
    i += 1
print("Max element:", max_elem)

# 5-masala

x = [1, 2, 3, 14, 5, 6, 6, 7]
max_elem = x[0]
max_index = 0
i = 1
while i < len(x):
    if x[i] > max_elem:
        max_elem = x[i]
        max_index = i
    i += 1
print("Index of max element:", max_index)

# 6-masala

num = int(input("Enter a number: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Number of digits:", count)

# 7-masala

x = [1, 2, 0, 14, 5, -6]
max_elem = x[0]
min_elem = x[0]
i = 1
while i < len(x):
    if x[i] > max_elem:
        max_elem = x[i]
    if x[i] < min_elem:
        min_elem = x[i]
    i += 1
print("Max element:", max_elem)
print("Min element:", min_elem)

# 8-masala

x = [-2, 31, 104, 51, 19, 7]
max_elem = x[0]
min_elem = x[0]
max_index = 0
min_index = 0
i = 1
while i < len(x):
    if x[i] > max_elem:
        max_elem = x[i]
        max_index = i
    if x[i] < min_elem:
        min_elem = x[i]
        min_index = i
    i += 1
x[max_index], x[min_index] = x[min_index], x[max_index]
print("List after swap:", x)

# 9-masala

x = [1, 2, 3, 4, 5]
num = int(input("Enter a number to search: "))
found = False
i = 0
while i < len(x):
    if x[i] == num:
        found = True
        break
    i += 1
if found:
    print("Element found")
else:
    print("Element not found")

# 10-masala

A = int(input("Enter A: "))
B = int(input("Enter B: "))
while B != 0:
    A, B = B, A % B
print("EKUB:", A)

# 11-masala

A = int(input("Enter A: "))
B = int(input("Enter B: "))
original_A = A
original_B = B
while B != 0:
    A, B = B, A % B
gcd = A
lcm = (original_A * original_B) // gcd
print("EKUK:", lcm)
