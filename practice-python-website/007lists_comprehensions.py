#This program takes an array and returns all the even elements in a comprehension list
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [item for item in a if item % 2 == 0]
print(b)