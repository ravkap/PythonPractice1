import sys
import random
from enum import Enum


def gn_game(name):
    game_count = 0
    your_wins = 0
    computer_wins = 0

    def play_gn():
        nonlocal name
        nonlocal your_wins
        nonlocal computer_wins

        class GN(Enum):
            One = 1
            Two = 2
            Three = 3

        playerchoice = input(
            f'\n{name}, try to guess what number i am thinking of... 1, 2, or 3.')
        if playerchoice not in ["1", "2", "3"]:
            print(f"\n{name}, please choose 1, 2 , or 3. ")
            return play_gn()

        player = int(playerchoice)

        computer_choice = random.choice("123")

        computer = int(computer_choice)

        print(f"\n{name}, you chose {
              str(GN(player)).replace('GN.', '').title()}.")
        print(f"Computer chose {
              str(GN(computer)).replace('GN.', '').title()}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal your_wins
            nonlocal computer_wins
            if player == 1 and computer == 2:
                computer_wins += 1
                return (f"Sorry {name}, You guessed incorrectly!😒")
            if player == 1 and computer == 3:
                computer_wins += 1
                return (f"Sorry {name}, You guessed incorrectly!😒")
            if player == 2 and computer == 1:
                computer_wins += 1
                return (f"Sorry {name}, You guessed incorrectly!😒")
            if player == 2 and computer == 3:
                computer_wins += 1
                return (f"Sorry {name}, You guessed incorrectly!😒")
            if player == 3 and computer == 1:
                computer_wins += 1
                return (f"Sorry {name}, You guessed incorrectly!😒")
            if player == 3 and computer == 2:
                computer_wins += 1
                return (f"Sorry {name}, You guessed incorrectly!😒")
            elif player == computer:
                your_wins += 1
                return (f"🎉Congratulations {name}, You guessed correctly!!!")

        game_result = decide_winner(player, computer)

        print(game_result)
        nonlocal game_count
        game_count += 1
        print(f"\nGame Count: {(game_count)}")
        print(f"\n{name}'s Wins: {(your_wins)}")
        print(f"\nComputer Wins: {(computer_wins)}")

        print(f"Play again, {name}?")

        while True:

            playagain = input(
                "\nPlay again? \n Y for Yes or \nQ to Quit to Arcade Menu.")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_gn()
        else:
            print("\nReturning to the Arcade Menu...\n")
            return
    return play_gn


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

    guess_number = gn_game(args.name)

    guess_number()

if __name__ == "__main__":
    guess_number()
