# 1-masala

n = 5
k = 3
for i in range(n):
    print(k)

# 2-masala

a = 2
b = 5
count = 0
for i in range(a, b + 1):
    print(i)
    count += 1
print("Jami sonlar:", count)

# 3-masala

a = 2
b = 5
count = 0
for i in range(b, a - 1, -1):
    print(i)
    count += 1
print("Jami sonlar:", count)

# 4-masala

price_per_kg = 5.5
for i in range(1, 11):
    print(i, "kg:", price_per_kg * i)

# 5-masala

price_per_kg = 5.5
for i in range(1, 11):
    print(i / 10, "kg:", price_per_kg * (i / 10))

# 6-masala

price_per_kg = 5.5
for i in range(12, 21, 2):
    print(i / 10, "kg:", price_per_kg * (i / 10))

# 7-masala

a = 2
b = 5
summa = 0
for i in range(a, b + 1):
    summa += i
print("Yig'indisi:", summa)

# 8-masala

a = 2
b = 5
product = 1
for i in range(a, b + 1):
    product *= i
print("Ko'paytmasi:", product)

# 9-masala

a = 2
b = 5
sum_of_squares = 0
for i in range(a, b + 1):
    sum_of_squares += i ** 2
print("Kvadratlar yig'indisi:", sum_of_squares)

# 10-masala

n = 5
summation = 0
for i in range(1, n + 1):
    summation += 1 / i
print("Yig'indi S =", summation)

# 11-masala

n = 5
sum_of_squares = 0
for i in range(1, n + 1):
    sum_of_squares += i ** 2
print("Kvadratlar yig'indisi:", sum_of_squares)

# 12-masala

n = 5
product = 1
for i in range(1, n + 1):
    product *= i
print("Ko'paytma S =", product)

# 13-masala

n = 5
alternating_sum = 0
for i in range(1, n + 1):
    alternating_sum += (-1)**(i+1) * i
print("Alternativ yig'indi S =", alternating_sum)

# 14-masala

n = 5
for i in range(1, n + 1):
    print(i, "ning kvadrati:", i ** 2)

# 15-masala

a = 2
n = 3
result = 1
for i in range(n):
    result *= a
print(a, "ning", n, "-darajasi:", result)

# 16-masala

a = 2
n = 3
for i in range(1, n + 1):
    print(a, "ning", i, "-darajasi:", a ** i)

# 17-masala

a = 2
n = 3
sum_powers = 0
for i in range(1, n + 1):
    sum_powers += a ** i
print("Yig'indisi:", sum_powers)

# 18-masala

a = 2
n = 3
alternating_sum = 0
for i in range(1, n + 1):
    alternating_sum += (-1)**(i+1) * (a ** i)
print("Alternativ yig'indisi:", alternating_sum)

# 19-masala

n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(n, "!", "=", factorial)

# 20-masala

n = 5
sum_factorials = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    sum_factorials += factorial
print("Yig'indi:", sum_factorials)
