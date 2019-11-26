lower_limit_a = int(input())
upper_limit_a = int(input())
lower_limit_b = int(input())
upper_limit_b = int(input())
random_number = 0

a = []
b = []
c = []

for i in range(lower_limit_a, lower_limit_b):
    random_number = random.randrange(100)
    a.append(random_number)
    print(a)



for item in a:
    if item in c:
        c.pop()
    if item in b:
        c.append(item)



print(c)