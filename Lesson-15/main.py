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

k = 1
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{k:02}", end=" ")
        k += 1
    print()


row = int(input("Row: "))
column = int(input("Column: "))

for i in range(1, row + 1):
    for j in range(1, column + 1):
        if (
            i == j or j + i == column + 1
        ):
            print(j, end=" ")
        else:
            print("*", end=" ")
    print()

row = int(input("Row: "))
column = int(input("Column: "))

for i in range(1, row + 1):
    for j in range(1, column + 1):
        if (
            i + j <= row + 1
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

row = int(input("Row: "))
column = int(input("Column: "))

for i in range(1, row + 1):
    for j in range(1, column + 1):
        if (
            i + j >= row + 1
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

row = int(input("Row: "))
column = int(input("Column: "))

for i in range(1, row + 1):
    for j in range(1, column + 1):
        if (
            i <= j
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

import time
import os

while True:
    os.system('clear')
    print("🔴\n⚪️\n⚪️")
    time.sleep(20)

    os.system('clear')
    print("🔴\n🟡\n⚪️")
    time.sleep(5)

    os.system('clear')
    print("⚪️\n⚪️\n🟢")
    time.sleep(20)

    os.system('clear')
    print("⚪️\n🟡\n⚪️")
    time.sleep(5)
