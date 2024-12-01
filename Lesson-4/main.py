# 1-masala
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

del fruits[1]
del fruits[2]

print(fruits)

# 2-masala
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

del numbers[1::2]

print(numbers)

# 3-masala
my_list = [10, 20, 30, 40, 50, 60, 70, 80]

del my_list[3:6]

print(my_list)

# 4-masala
cities = ["New York", "London", "Tokyo", "Moscow", "Paris"]

cities.pop(2)

print(cities)

# 5-masala
numbers = [5, 10, 15, 20, 25]

numbers.pop(0)
numbers.pop(-1)

print(numbers)

# 6-masala
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits = ["banana"]

print(fruits)

# 7-masala
items = [1, 2, 3, 4, 5]

del items

print(items)

# 8-masala
cars = ["Toyota", "Ford", "BMW", "Audi"]

cars.append(cars.pop(1))

print(cars)

# 9-masala
numbers = [1, 2, 3, 4, 5]

numbers = numbers[::-1]

print(numbers)