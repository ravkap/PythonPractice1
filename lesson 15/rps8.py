import sys
import random
from enum import Enum


def rps(name='Player_1'):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    tie_game = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal tie_game

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        print("")
        playerchoice = input(
            f'\n{name}, enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n')
        if playerchoice not in ["1", "2", "3"]:
            print(f"\n{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computer_choice = random.choice("123")

        computer = int(computer_choice)

        print(f"\n{name}, you chose  {
              str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Computer chose  {
              str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal tie_game
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, You Win! "
            elif player == 2 and computer == 1:
                player_wins += 1

                return f"🎉 {name}, You Win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, You Win!"
            elif player == computer:
                tie_game += 1
                return "🐱‍👤Tie Game!"

            else:
                computer_wins += 1
                return f"😒 Computer Wins, sorry {name}."

        game_result = decide_winner(player, computer)

        print(game_result)
        nonlocal game_count
        game_count += 1
        print(f"\nGame Count: {(game_count)}")
        print(f"\n{name}'s Wins: {(player_wins)}")
        print(f"\nComputer Wins: {(computer_wins)}")
        print(f"\nTie Games: {(tie_game)}")

        print(f"\nPlay Again, {name}?")

        while True:

            playagain = input("\nPlay Again? \nY for Yes or \nQ to Quit\n\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Byeeeee {name}! ❤")

    return play_rps


if __name__ == "__main__":
    import argparse

    parcer = argparse.ArgumentParser(
        description="Provides a personalized Game expeience"
    )

    parcer.add_argument(
        "-n", "--name", metavar="name",
        required=True, help=" the name of the perosn pplaying the game."

    )

    args = parcer.parse_args()

    rock_paper_scissors = rps(args.name)

    rock_paper_scissors()
