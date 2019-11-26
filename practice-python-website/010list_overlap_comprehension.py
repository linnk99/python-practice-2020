import random
#This program generates 2 random lists and compares common elements
print("This program generates two lists with single random elements and and random lenght.")
#Data input
a_upper_limit = int(input("What\'s max range of numbers in the first list? "))
b_upper_limit = int(input("What\'s max range of numbers in the second list? "))

#Processing the data
#Generates two random lists taking single numbers from 0 to 100
#The lenght of the lists are from 0 to the upper limits variables
a = random.sample(range(100), random.randrange(0,a_upper_limit))
b = random.sample(range(100), random.randrange(0,b_upper_limit))
c = []
d = [item for item in a if item in b and item not in c]

print("\nThis is the first list \n" + str(a) + "\n")
print("This is the second list \n" + str(b) + "\n")
print("These are the common elements\n" + str(d))