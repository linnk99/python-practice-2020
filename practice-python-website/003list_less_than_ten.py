#This program asks for a number and returns all the numbers smaller than it from the list

#Data input and creation of the list
check = int(input("Pick a number and you\'ll get the elements smaller than this "))
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_check = []

#Data processing
for element in range(0, len(numbers)):
    if numbers[element] < check:
        #print("The number " + str(numbers[element]) + " is less than 5")
        less_than_check.append(numbers[element])

#Data output
print("The numbers smaller than " + str(check) + " are: " + str(less_than_check))