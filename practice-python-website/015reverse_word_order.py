##This is a comment

def split_string(sentence):
    sentence = sentence.split()
    #print(sentence)
    sentence.reverse()
    #print(sentence)
    return " ".join(sentence)
    
    

print("This program reverse the order of the sentence given.")
sentence = str(input("Enter a sentence of more than two words to reverse: "))


result = split_string(sentence)
print(result)