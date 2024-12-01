days = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]

for week in range(1, 5):
    print(f"hafta: {week}")
    for day in range(0, 7):
        print(f"\t {days[day]}")

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 6):
        if j == 1:
            print("0", end=" ")
        else:
            print("*", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 6):
        if j == 1 or i == 1:
            print("0", end=" ")
        else:
            print("*", end=" ")
    print()

row = int(input("Row: "))
column = int(input("Column: "))

for i in range(1, row + 1):
    for j in range(1, column + 1):
        if j == 1 or i == 1 or j == column or i == row:
            print("0", end=" ")
        else:
            print("*", end=" ")
    print()

row = int(input("Row: "))
column = int(input("Column: "))

ortaRow = row // 2 + 1
ortaCol = column // 2 + 1

for i in range(1, row + 1):
    for j in range(1, column + 1):
        if i == ortaRow or j == ortaCol:
            print(i, end=" ")
        else:
            print("", end=" ")
    print()