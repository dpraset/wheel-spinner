import random

# initialize wheel
def wheel():
    inputnames = input("Enter wheel inputs separated by semi-colons: ").strip()

    if not inputnames:
        print("No names entered. Exiting.")
        return
    
    inputlist = [name.strip() for name in inputnames.split(';') if name.strip()]

    if not inputlist:
        print("No valid names entered. Exiting.")
        return

    while inputlist:
        print("\nSpinning the wheel...\n")
        winner = random.choice(inputlist)

        print(f"🎉 The winner is: {winner}! 🎉")

        # Ask if the winner should be removed
        remove_winner = input(f"Do you want to remove {winner} from the list? (y/n): ").strip().lower()
        if remove_winner == "y":
            inputlist.remove(winner)
            print(f"{winner} has been removed from the list.")

        if not inputlist:
            print("All names have been selected or removed. Exiting.")
            break
        
        print("\nRemaining participants:")
        for name in inputlist:
            print(f"- {name}")

        # Play again feature
        play_again = input("\nDo you want to spin the wheel again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Exiting wheel spinner.")
            break

if __name__ == "__main__":
    wheel()