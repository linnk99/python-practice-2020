#This program receives a string and checks if it's a palindrome
#Data input
phrase = str(input("Enter a word or phrase to check if it is a palindrome or not: "))

#Checking if it's a palindrome
reverse_phrase = phrase[::-1]

#Output result
if phrase == reverse_phrase:
    print(phrase + " is a palindrome")
else:
    print(phrase + " is NOT a palindrome")