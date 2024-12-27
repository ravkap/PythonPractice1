from rps9 import rps
from guess_number import gn_game
from enum import Enum
import sys


def arcade_hub(name):
    game_count = 0
    game2_count = 0

    def arcade():
        nonlocal name
        nonlocal game_count
        nonlocal game2_count

    class ARCADE(Enum):
        RPS = 1
        GN = 2

    playerchoice = input(
        f"\nHello {name} choose what game you'd like to play."
        "\n1 for Rock, Paper, Scissors."
        "\n2 for Guess my Number Game."
    )
    if playerchoice not in ["1", "2"]:
        print(f"\nPlease choose one of the available games by entering 1, or 2.")
        return arcade_hub(name)

    if playerchoice == "1":
        print("\nStarting Rock, Paper, Scissors!")
        game = rps(name)
        game()
    elif playerchoice == "2":
        print("\nStarting Guess My Number Game!")
        game = gn_game(name)
        game()

    while True:

        playagain = input(
            "\nBack to the Arcade? \nY for Yes or \nQ to Quit\n\n")
        if playagain.lower() not in ["y", "q"]:
            print("Invalid input. Please enter Y for Yes or Q for Quit.")
            continue
        if playagain.lower() == "y":
            return arcade_hub(name)  # Restart the game selection
        else:
            print("\n🎉🎉")
            print(f"Thank you for playing, {name}!\n")
            sys.exit(f"Byeeeee {name}! ❤")


if __name__ == "__main__":
    import argparse

    parcer = argparse.ArgumentParser(
        description="Provides a personalized Game expeience"
    )

    parcer.add_argument(
        "-n", "--name", metavar="name",
        required=True, help=" the name of the person playing the game."

    )

    args = parcer.parse_args()

    arcade = arcade_hub(args.name)
