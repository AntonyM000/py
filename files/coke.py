# tuples dictionary loops
# In a file called coke.py, implement a program that prompts the user to insert a coin,
# one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

def coke():
    value=input("Insert coin value in cents")
    if str(value) <50:
        print(value)
    else: 