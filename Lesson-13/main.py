# 1-masala

my_list = [1, 2, 3, 0, 5, 6, 7, 9]
toq = []
juft = []

for x in my_list:
    if x % 2 == 0:
        if x != 0:
            juft.append(x)
    else:
        toq.append(x)

print(toq)
print(juft)

# 2-masala

a = [1, 5, 6, 3, 2, 1, 6, 7]
b = []

for x in range(len(a) - 1):
    b.append(a[x] + a[x + 1])
print(b)

a = ['olma', 'nok', 'limon', 'gilos']
b = []

for x in a:
    b.append(len(x))

print(b)

a = [1, 5, 4, 3, 2, 1, 7, 5, 4, 3]
b = []


for i in range(len(a) // 2):
    b.append(a[i] + a[-(i + 1)])

print(b)
