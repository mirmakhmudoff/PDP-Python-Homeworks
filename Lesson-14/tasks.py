input_row = int(input("Row: "))
input_column = int(input("Column: "))

for i in range(1, input_row+1):
    for j in range(1, input_column+1):
        if (
            j == 1
            or (i == 1 and j != input_column)
            or (i == input_row // 2 + 1 and j != input_column)
            or (i == input_row // 2  and j == input_column-1)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

row = int(input("Row: "))
column = int(input("Column: "))

for i in range(1, row + 1):
    for j in range(1, column + 1):
        if i == j:
            print(i, end="")
        else:
            print(" ", end="")
    print()

row = int(input("Row: "))
column = int(input("Column: "))

ortaRow = row // 2 + 1
ortaColumn = column // 2 + 1

for i in range(1, row + 1):
    for j in range(1, column + 1):
        if (ortaRow == i or ortaColumn == j or ortaRow == i + 1 or ortaColumn == j + 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

row = 5
column = 5

for i in range(1, row + 1):
    for j in range(1, column + 1):
        if (
            (i == j)
            or (j + i == column + 1)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()