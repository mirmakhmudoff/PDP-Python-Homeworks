n = int(input("n ni kiriting: "))

a = 0
b = 1

while a <= n:
    print(a)
    a, b = b, a + b
