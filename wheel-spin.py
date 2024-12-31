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
    
    # play again feature with winner removed
        play_again = input("Do you want to spin the wheel again? (y/n): ")
        if play_again.lower() != "y":
            print("Exiting wheel spinner.")
            break

if __name__ == "__main__":
    wheel()