# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, 
# and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
#  If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
#  And if 99% or more remains, output F instead to indicate that the tank is essentially full.
# from fractions import Fraction

def to_percentage(fraction):
 
 num,den = map(int, fraction.split("/"))
 try:
    if num > den or den == 0 :
        #  pass    
         return None
    percentage=num/den*100
    if percentage <=1:
      return 'E'
    elif percentage>=99:
      return 'F'
    else:
      return round(percentage) 
 except(ValueError,ZeroDivisionError):
   pass

def main(): 
 fraction=input("What's the value of fuel in the tank as a fraction?")
 percentage=to_percentage(fraction)
 if percentage is None:
   pass
 else:
    print(percentage)


main()