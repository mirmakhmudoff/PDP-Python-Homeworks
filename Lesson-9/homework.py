n = int(input("Xonalar sonini kiriting: "))

start = 10**(n-1)
end = 10**n - 1
i = start

while i <= end:
    print(i)
    i += 1
