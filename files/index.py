def ask_input ():
    age=input("What's your age ")
    # age=input(age)
    if int(age)>16:
        print("You can drive")
    elif int(age)<=16:
        print("You can't drive")
    else:
        print("invalid number")


ask_input()

