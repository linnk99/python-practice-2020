def get_integer():
    return int(input("Pick a number to know if it\'s prime or not: "))

def find_prime(number, divisors):
    for i in range(1, number):
        if number % i == 0:
            divisors += 1
        else:
    if divisors == 2 or number == 1:
         print("The number " + str(number) + " is prime!")
    else:
        print("The number " + str(number) + " isn\'t prime!")

divisors = 1

print("This number determines if a number is prime or no")
number = get_integer()

find_prime(number, divisors)