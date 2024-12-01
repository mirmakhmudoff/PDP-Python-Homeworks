my_set = {1, 2, 5, 4, 6, 9, 5}
my_set.add(10)
print(my_set)

matrix = [
    [1,23,45,89,90],
    [-6,56,34,12,0],
    [1,3,4,2,8,6]
]

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        print(f"{matrix[i][j]:2}", end=" ")
    print()
    max_num = 0
    for k in matrix[i]:
        if k > max_num:
            k = max_num
        print(max_num)
