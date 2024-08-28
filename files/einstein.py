# joulesmass=int(mass) * 89875517873681764
 #  # print(f"You are {joulesmass}joules")
# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) 
# and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
# One kilogram (kg) of mass is equivalent to exactly 89,875,517,873,681,764 joules
def convert_mass_to_joules():
    mass=input("What's your weight in kgs?")
    c = 300000000
    E = int(mass) * c * c
    print(f"E {E} joules")


convert_mass_to_joules()