# implement a program that prompts the user for items, 
# one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). 
# Then output the user’s grocery list in all uppercase,
# sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. 
# No need to pluralize the items.
# Treat the user’s input case-insensitively.
state= 1
grocery_item=''
while state <4:
    grocery_item+=input("Input grocery item")
    state+=1
print(grocery_item)

