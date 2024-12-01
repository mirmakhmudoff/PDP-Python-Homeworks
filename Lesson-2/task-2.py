bmw = 15000
mers = 6000
ferrari = 13000
tesla = 10000

print(f"BMW: {bmw}")
print(f"Mers: {mers}")
print(f"Ferrari: {ferrari}")
print(f"Tesla: {tesla}")

summa = int(input("Enter the amount: "))

not_enought = summa - bmw
not_enought1 = summa - mers
not_enought2 = summa - ferrari
not_enought3 = summa - tesla

print(f"BMW: {summa >= bmw} {not_enought}")
print(f"Mers: {summa >= mers} {not_enought1}")
print(f"Ferrari: {summa >= ferrari} {not_enought2}")
print(f"Tesla: {summa >= tesla} {not_enought3}")