import random

# initialize wheel 
def wheel():
    inputnames = input("Enter wheel inputs separated by semi-commas: ")
    inputlist = inputnames.split(';')

    while inputlist:
        print("\nSpinning the wheel...\n")
        winner = random.choice(inputlist)

        print(f"🎉 The winner is: {winner}!")

        # ask user to remove winner prompt
        remove_winner = input(f"Do you want to remove {winner} from the list? (y/n): ").strip().lower()
        if remove_winner == "y":
            inputlist.remove(winner)
            print(f"{winner} has been removed from the list.")

        if not inputlist:
            print("All names have been selected or removed. Exiting wheel spinner")
            break
        
        print("\nRemaining participants:")
        for name in inputlist:
            print(f"- {name}")
    
    # play again feature with winner removed
        play_again = input("Do you want to spin the wheel again? (y/n): ")
        if play_again.lower() != "y":
            print("Exiting wheel spinner.")
            break

if __name__ == "__main__":
    wheel()