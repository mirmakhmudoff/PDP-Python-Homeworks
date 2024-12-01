a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))

i = 1
sum_a = 0
while i <= a // 2:
    if a % i == 0:
        sum_a += i
    i += 1

j = 1
sum_b = 0
while j <= b // 2:
    if b % j == 0:
        sum_b += j
    j += 1

if sum_a == b and sum_b == a:
    print("Sonlar do'st sonlar")
else:
    print("Sonlar do'st sonlar emas")
