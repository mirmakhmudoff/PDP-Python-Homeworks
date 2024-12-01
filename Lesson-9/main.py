start = int(input("1-sonni kiriting: "))
stop = int(input("2-sonni kiriting: "))

if start < stop:
    while start <= stop:
        print(start)
        start += 1
else:
    while stop <= start:
        print(start)
        start += 1
