# In a file called faces.py, implement a function called convert that accepts a str as input 
# and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) 
# and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.
          

def convert():
    hstring=input("What's your car brand? And emoji ")
    grinningface= 'U0001f600'
    # print(hstring.replace(":)","\N{grinningface}").replace(":(","\U0001F606"))
    print(hstring.replace(":)",{grinningface}).replace(":(","\U0001F606"))
    # print(hstring.replace(":)","\U0001f600"))

convert()
