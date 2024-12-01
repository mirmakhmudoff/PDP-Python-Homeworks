# 1-masala

num = int(input("3 xonali son kiriting: "))

x = num // 100
z = num // 10 % 10
y = num % 10

summa = x + y

check = summa == x or summa == y or summa == z

print(check)

# 2-masala

num = int(input("3 xonali son kiriting: "))

x = num // 100
y = num % 10

check = x > y

print(check)

# 3-masala

enterprice = int(input("Enter the Enterprise in IT science: "))
its = int(input("Enter the ITS science: "))
programming = int(input("Enter the Programming science: "))
english = int(input("Enter the English science: "))
web = int(input("Enter the Web science: "))

x = (enterprice + its + programming + english + web) / 5

print(x >= 4.5)
