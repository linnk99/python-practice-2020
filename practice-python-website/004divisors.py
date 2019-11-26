#This program return all the prime numbers from the input

#Data input
number = int(input("Choose a number to know all of its divisors: "))
divisors = []

#Data processing
for i in range (1, number):
    if number % i == 0:
        divisors.append(i)

#Data output
print("The divisors of " + str(number) + "are " + str(divisors))