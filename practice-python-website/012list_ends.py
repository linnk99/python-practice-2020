import random

def list_generator(random_lenght, numbers):
    for i in range(1, random_lenght):
        numbers.append(i)
    print(numbers)

def list_first_and_last(numbers):
    first_and_last.append(numbers[0])
    first_and_last.append(numbers[-1])
    print(first_and_last)

numbers = []
first_and_last = []
random_lenght = random.randint(1, 100)

list_generator(random_lenght, numbers)
list_first_and_last(numbers)