import math

num = float(input("Musbat son kiriting: "))

if num >= 0:
    sqrt = math.sqrt(num)
    print(f"{num} sonining kvadrat ildizi: {sqrt}")
else:
    print("Iltimos, musbat son kiriting.")