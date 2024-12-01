input_row = int(input("Row: "))
input_column = int(input("Column: "))

for i in range(1, input_row+1):
    for j in range(1, input_column+1):
        if (
           (j != 1 and j != input_column and i == 1)
            or (j == input_column - 1)
            or  (j != 1 and j != input_column and i == input_row)
            or (i == input_row - 1 and j ==  2)
            or (i == input_row and j ==  2)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\n")

for row in range(input_row):
    for col in range(input_column):
        if (
                (row == 0 and col != 0 and col != input_column - 1)
                or (col == 0 and row != 0)
                or (row == input_row // 2)
                or (row != 0 and col == input_column - 1)
            ):
            print("*", end="")
        else:
            print(end=" ")
    print()
print("\n")

for i in range(1, input_row+1):
    for j in range(1, input_column+1):
        if (
             (i == j and j <= input_column // 2+1 and i <= input_row // 2+1)
            or ( j == (input_column - i + 1) and i <= input_row // 2+1 )
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\n")

for i in range(1, input_row+1):
    for j in range(1, input_column+1):
        if (
         (j == 1 and i != 1 and i != input_row)
            or (i == 1 and j != 1 and j != input_column)
            or ( j == input_column and i != 1 and i != input_row)
            or (i == input_row and j != 1 and j != input_column)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\n")

for i in range(1, input_row+1):
    for j in range(1, input_column+1):
        if (
             (i == j )
            or ( j == (input_column - i + 1)  )
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\n")

for i in range(1, input_row+1):
    for j in range(1, input_column+1):
        if (
           ( i == 1 and j != 1 and j != input_row)
            or j == input_column // 2 + 1
            or
            (i == input_row and j != 1 and j != input_row)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\n")

for row in range(input_row):
    for col in range(input_column):
        if (
            col == 0
            or (row == 0 and col != input_column - 1)
            or (row == input_row // 2 and col != input_column - 1)
            or (col == input_column - 1 and row != 0 and row != input_row // 2 and row != input_row - 1)
            or (row == input_row -1 and col == input_column - 1)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\n")
