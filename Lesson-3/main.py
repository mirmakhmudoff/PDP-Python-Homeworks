# 1-masala
m = int(input("Kg kiriting "))
result = m / 1000
print(f"Shuncha Tonna bo'ladi {result}")

# 2-masala
kb = int(input("Bayt kiriting: "))
result = kb / 1024
print(f"Shuncha KB bo'ladi: {result}")

# 3-masala
a = int(input("A kesmaning sonini kiriting: "))
b = int(input("B kesmaning sonini kiriting: "))
result = a // b
check = a % b
print(f"A kesmani B kesmaga {result} martta joylashtirish mumkin, Ortib qolgan qismi {check}")

# 4-masala
son = int(input("Sonni kiriting: "))
x = son // 10
y = son % 10
print(f"O'nlar xonasi {x}, Birliklar xonasi {y}")

# 5-masala
a = int(input("A kesmaning musbat sonini kiriting: "))
b = int(input("B kesmaning musbat sonini kiriting: "))
result = a // b
check = a % b
print(f"A kesmani B kesmaga {result} martta joylashtirish mumkin, Ortib qolgan qismi {check}")

# 6-masala
son = int(input("Uch xonali sonni kiriting: "))
x = son // 100
y = (son // 10) % 10
z = son % 10
print(f"Yuzlar xonasi {x}, O'nlar xonasi {y}, Birliklar xonasi {z}")

# 7-masala
son = int(input("Sonni kiriting: "))
x = son // 10
y = son % 10
z = x + y
print(f"Raqamlar yig'indisi {z}")

# 8-masala
son = int(input("Sonni kiriting: "))
x = son // 10
y = son % 10
check = f"{y}{x}"
num = int(check)
print(num)
print(type(num))

# 9-masala
son = int(input("Sonni kiriting: "))
x = son // 100
print(f"Yuzlar xonasi {x}")

# 10-masala
x = int(input("Sonni kiriting: "))
onlar = x // 10 % 10
yuzlar = x // 100 % 10
print(f"Yuzlar xonasidagi son {yuzlar}, O'nlar xonasidagi son {onlar}")

# 11-masala
number = 123
hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10
result = hundreds + tens + ones
print(result)

# 12-masala
number = 123
hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10
reversed_number = ones * 100 + tens * 10 + hundreds
print(reversed_number)

# 13-masala
number = 123
hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10
result = tens * 100 + ones * 10 + hundreds
print(result)

# 14-masala
number = 123
hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10
result = ones * 100 + hundreds * 10 + tens
print(result)

# 15-masala
number = 123
hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10
result = hundreds * 100 + ones * 10 + tens
print(result)

# 16-masala
number = 123
hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10
result = tens * 100 + hundreds * 10 + ones
print(result)

# 17-masala
number = 1234
hundreds = (number // 100) % 10
print(hundreds)

# 18-masala
number = 123456
first_three_digits = number // 1000
print(first_three_digits)

# 19-masala
seconds = int(input("N sekund kiriting: "))
minutes = seconds // 60
print(f"Shuncha minut o'tdi: {minutes}")

# 20-masala
seconds = int(input("N sekund kiriting: "))
hours = seconds // 3600
print(f"Shuncha soat o'tdi: {hours}")

# 21-masala
seconds = int(input("N sekund kiriting: "))
minutes = seconds // 60
remaining_seconds = seconds % 60
print(f"Minutes: {minutes}, Seconds: {remaining_seconds}")

# 22-masala
seconds = int(input("N sekund kiriting: "))
hours = seconds // 3600
remaining_seconds = seconds % 3600
print(f"Hours: {hours}, Remaining Seconds: {remaining_seconds}")

# 23-masala
seconds = int(input("N sekund kiriting: "))
hours = seconds // 3600
remaining_seconds = seconds % 3600
minutes = remaining_seconds // 60
remaining_seconds = remaining_seconds % 60
print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {remaining_seconds}")
