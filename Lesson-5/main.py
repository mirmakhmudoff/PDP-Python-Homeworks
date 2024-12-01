# 1-masala
fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi')

print(f"First element: {fruits[0]}")
print(f"Last element: {fruits[-1]}")
print(f"Third element: {fruits[2]}")

# 2-masala
numbers = (1, 2, 3, 4, 2, 5, 6, 2)
count = numbers.count(2)

print(f"Number of twos: {count}")
index = numbers.index(5)
print(f"Index of 5: {index}")

# 3-masala
colors = ('red', 'green', 'blue')
colors_list = list(colors)
colors_list.append('yellow')

print(colors_list)

colors_tuple = tuple(colors_list)

print(colors_tuple)

# 4-masala
letters = ('a', 'b', 'c', 'd', 'e')
reversed_letters = letters[::-1]

print(reversed_letters)

# 5-masala
nested_tuple = (1, 2, (3, 4, 5), 6, 7)
second_element = nested_tuple[2][1]

print(f"Second element of inner tuple: {second_element}")

for element in nested_tuple:
    print(element)

# 6-masala
my_tuple = (10, 20, 30, 40, 50)
my_list = list(my_tuple)
my_list.append(60)

print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

#  7-masala
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2

print(combined_tuple)
