# 1-masala

x = int(input("Enter a number: "))
if x > 0:
    x += 1
print(x)

# 2-masala

x = int(input("Enter a number: "))
if x > 0:
    x += 1
else:
    x -= 2
print(x)

# 3-masala

x = int(input("Enter a number: "))
if x > 0:
    x += 1
elif x < 0:
    x -= 2
else:
    x = 10
print(x)

# 4-masala

a, b, c = int(input("Enter integer a: ")), int(input("Enter integer b: ")), int(input("Enter integer c: "))
positive_count = 0
if a > 0:
    positive_count += 1
if b > 0:
    positive_count += 1
if c > 0:
    positive_count += 1
print(positive_count)

# 5-masala

a, b, c = int(input("Enter integer a: ")), int(input("Enter integer b: ")), int(input("Enter integer c: "))
positive_count, negative_count = 0, 0
if a > 0:
    positive_count += 1
elif a < 0:
    negative_count += 1
if b > 0:
    positive_count += 1
elif b < 0:
    negative_count += 1
if c > 0:
    positive_count += 1
elif c < 0:
    negative_count += 1
print("Positive count:", positive_count)
print("Negative count:", negative_count)

# 6-masala

a, b = int(input("Enter integer a: ")), int(input("Enter integer b: "))
if a > b:
    print(a)
else:
    print(b)

# 7-masala

a, b = int(input("Enter integer a: ")), int(input("Enter integer b: "))
if a < b:
    print("Order:", a, b)
else:
    print("Order:", b, a)

# 8-masala

a, b = int(input("Enter integer a: ")), int(input("Enter integer b: "))
if a > b:
    print("Larger first:", a, b)
else:
    print("Larger first:", b, a)

# 9-masala

A, B = float(input("Enter real number A: ")), float(input("Enter real number B: "))
if A > B:
    A, B = B, A
print("A:", A, "B:", B)

# 10-masala

A, B = int(input("Enter integer A: ")), int(input("Enter integer B: "))
if A != B:
    A = B = A + B
else:
    A = B = 0
print("A:", A, "B:", B)

# 11-masala

A, B = int(input("Enter integer A: ")), int(input("Enter integer B: "))
if A != B:
    if A > B:
        B = A
    else:
        A = B
else:
    A = B = 0
print("A:", A, "B:", B)

# 12-masala

a, b, c = int(input("Enter integer a: ")), int(input("Enter integer b: ")), int(input("Enter integer c: "))
print("Smallest:", min(a, b, c))

# 13-masala

a, b, c = int(input("Enter integer a: ")), int(input("Enter integer b: ")), int(input("Enter integer c: "))
if (b < a < c) or (c < a < b):
    print(a)
elif (a < b < c) or (c < b < a):
    print(b)
else:
    print(c)

# 14-masala

a, b, c = int(input("Enter integer a: ")), int(input("Enter integer b: ")), int(input("Enter integer c: "))
if a < b:
    if b < c:
        print(a, b, c)
    else:
        if a < c:
            print(a, c, b)
        else:
            print(c, a, b)
else:
    if a < c:
        print(b, a, c)
    else:
        if b < c:
            print(b, c, a)
        else:
            print(c, b, a)

# 15-masala

a, b, c = int(input("Enter integer a: ")), int(input("Enter integer b: ")), int(input("Enter integer c: "))
print("Sum of largest two:", a + b + c - min(a, b, c))

# 16-masala

A, B, C = float(input("Enter real number A: ")), float(input("Enter real number B: ")), float(input("Enter real number C: "))
if A < B < C:
    A *= 2
    B *= 2
    C *= 2
else:
    A = -A
    B = -B
    C = -C
print("A:", A, "B:", B, "C:", C)

# 17-masala

A, B, C = float(input("Enter real number A: ")), float(input("Enter real number B: ")), float(input("Enter real number C: "))
if A < B < C or C < B < A:
    A *= 2
    B *= 2
    C *= 2
else:
    A = -A
    B = -B
    C = -C
print("A:", A, "B:", B, "C:", C)

# 18-masala
a, b, c = int(input("Enter integer a: ")), int(input("Enter integer b: ")), int(input("Enter integer c: "))
if a == b and b != c:
    print(3)
elif a == c and c != b:
    print(2)
elif b == c and a != c:
    print(1)

# 19-masala
a, b, c, d = int(input("Enter integer a: ")), int(input("Enter integer b: ")), int(input("Enter integer c: ")), int(input("Enter integer d: "))
if a == b == c and c != d:
    print(4)
elif a == b == d and b != c:
    print(3)
elif a == c == d and a != b:
    print(2)
elif b == c == d and a != b:
    print(1)

# 20-masala
A, B, C = int(input("Enter A: ")), int(input("Enter B: ")), int(input("Enter C: "))
AB = abs(B - A)
AC = abs(C - A)
print("Closest to A:", "B" if AB < AC else "C")

# 21-masala
x, y = int(input("Enter x coordinate: ")), int(input("Enter y coordinate: "))
if x == 0 and y == 0:
    print(0)
elif x == 0:
    print(1)
elif y == 0:
    print(2)
else:
    print(3)

# 22-masala
x, y = int(input("Enter x coordinate: ")), int(input("Enter y coordinate: "))
if x > 0 and y > 0:
    print("1st quadrant")
elif x < 0 and y > 0:
    print("2nd quadrant")
elif x < 0 and y < 0:
    print("3rd quadrant")
else:
    print("4th quadrant")

# 23-masala
x1, y1 = int(input("Enter x1: ")), int(input("Enter y1: "))
x2, y2 = int(input("Enter x2: ")), int(input("Enter y2: "))
x3, y3 = int(input("Enter x3: ")), int(input("Enter y3: "))
x4, y4 = x1, y2
print("Fourth vertex coordinates:", x4, y4)
