#This programs receives 2 numbers and compares them to know if the division returns an odd or even number

#Data input
number = int(input("Pick a number to check: "))
check = int(input("Pick a number to divide by: "))

#Data processing and output
""" if number % 4 == 0:
    print(str(number) + " is multiple of 4!") """
if number % check == 0:
    print(str(number) + " is divided evenly by " + str(check))
else:
    print(str(number) + " is divided oddly by " + str(check))