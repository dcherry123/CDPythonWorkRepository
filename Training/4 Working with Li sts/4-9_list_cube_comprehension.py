# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

squares = [value**3 for value in range(1,11)]

for i in squares:
    print(i)


# animals = [name.upper() for name in animals]