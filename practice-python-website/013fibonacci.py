
def fibonacci_numbers(lenght, numbers):
    for i in range(1, lenght):
        if len(numbers) == 1:
            numbers.append(1)
        else:
            numbers.append(numbers[-2] + numbers[-1])
    print(numbers)

numbers = [0]

lenght = int(input("How many numbers in the Fibonacci\'s series do you want to know? "))


fibonacci_numbers(lenght, numbers)