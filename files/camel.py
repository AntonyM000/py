""" In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case 
 and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel """
    # print(name.replace(" ","_").lower())

# def ccprogram():
name=input("What's your name in camelCase")
word = ''
for letter in name:
    if letter.isupper():
        word+= "_" + letter.lower()
    else:
        word+=letter
print (word)



# ccprogram()

# and
# or
# ==

# switch
# comparison operators