# 1-masala

my_list = [1, 2, 3, 4, 5]
element = 3
found = False
index = 0
while index < len(my_list):
    if my_list[index] == element:
        found = True
        break
    index += 1
print(found)


# 2-masala

number = 100
results = []
while number < 1000:
    x = number // 100
    y = (number // 10) % 10
    z = number % 10
    total = x + y + z
    if total > 5 and total < 8:
        results.append(number)
    number += 1
print(results)

3-masala

num = 777
count = 0
temp = num
while temp > 0:
    temp //= 10
    count += 1
print(count)

# 4-masala

numbers = [1, 2, 3, 4, 5]
total = 0
index = 0
length = len(numbers)
while index < length:
    total += numbers[index]
    index += 1


# 5-masala

numbers = [3, 9, 2, 8, 5]
max_value = numbers[0]
index = 1
length = len(numbers)
while index < length:
    if numbers[index] > max_value:
        max_value = numbers[index]
    index += 1

# 6-masala

numbers = [3, 9, 2, 8, 5]
min_value = numbers[0]
index = 1
length = len(numbers)
while index < length:
    if numbers[index] < min_value:
        min_value = numbers[index]
    index += 1


7-masala

original_list = [1, 2, 3, 4]
result_list = []
index = 0
length = len(original_list)
while index < length:
    result_list.append(original_list[index] * 2)
    index += 1
print(result_list)

# 8-masala

num = 28
divisor_sum = 0
divisor = 1
while divisor < num:
    if num % divisor == 0:
        divisor_sum += divisor
    divisor += 1
num = (divisor_sum == num)

# 9-masala

num = 16
power = 1
temp = 2
while temp < num:
    temp *= 2
    power += 1
if temp == num:
    result = f"{num} is 2 raised to the power {power}"
else:
    result = f"{num} is not a power of 2"

# 10-masala

num = 16
power = 0
temp = 1
while temp < num:
    temp *= 2
    power += 1
if temp == num:
    result = f"{num} is 2 raised to the power {power}"
else:
    result = f"{num} is not a power of 2"

# 11-masala

num = 5
factorial = 1
counter = num
while counter > 1:
    factorial *= counter
    counter -= 1

# 12-masala

x = [1, 23, 10, 45, -41, 56, 78, 13]
even_list = []
odd_list = []
index = 0
length = len(x)
while index < length:
    if x[index] % 2 == 0:
        even_list.append(x[index])
    else:
        odd_list.append(x[index])
    index += 1


# 13-masala

num = 5
multiplier = 1
result_table = []
while multiplier <= 10:
    print(f"{num} x {multiplier} = {num * multiplier}")
    multiplier += 1


# 14-masala

cars = ["Audi", "Toyota", "Mazda", "Volvo", "Lada"]
longest = cars[0]
index = 1
length = len(cars)
while index < length:
    if len(cars[index]) > len(longest):
        longest = cars[index]
    index += 1

# 15-masala

cars = ["Audi", "Toyota", "Mazda", "Volvo", "Lada"]
ending_a = []
index = 0
length = len(cars)
while index < length:
    if cars[index][-1] == 'a':
        ending_a.append(cars[index])
    index += 1


n = int(input("Nechta son kiritasiz: "))
i = 0
found = 0

while i < n:
    num = int(input("Son kiriting: "))
    if num > found or num < found:
        found = num
    i += 1

print("Sonlardan eng kattasi:", found)

