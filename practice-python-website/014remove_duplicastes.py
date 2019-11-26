import random

def list_generator(list_a, list_b, upper_limit):
    for i in range(0, upper_limit):
        list_a.append(random.randint(0, upper_limit))
        list_b.append(random.randint(0, upper_limit))
    
    print(list_a)
    print(list_b)

def remove_duplicates(list_a, list_b, list_c, upper_limit):
    for item in list_a:
        if item in list_b and item not in list_c:
            list_c.append(item)
    
    print(list_c)
    

list_a = []
list_b = []
list_c = []
upper_limit = int(input("Choose a limit for the range of the lists to be compared: "))

list_generator(list_a, list_b, upper_limit)
remove_duplicates(list_a, list_b, list_c, upper_limit)

