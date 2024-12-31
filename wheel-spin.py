import random

# initialize wheel 

def wheel():
    inputnames = input("Enter wheel inputs separated by semi-commas: ")
    inputlist = inputnames.split(';')

    while inputlist:
        print("Spinning the wheel...\n")
        winner = random.choice(inputlist)
        print("The winner is:", winner)
        inputlist.remove(winner)
