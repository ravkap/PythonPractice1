import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0
    tie_game = 0

    def play_rps():
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal tie_game

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        print("")
        playerchoice = input(
            '\nEnter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n')
        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computer_choice = random.choice("123")

        computer = int(computer_choice)

        print(f"\nYou chose  {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Computer chose  {
              str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal tie_game
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You Win! "
            elif player == 2 and computer == 1:
                player_wins += 1

                return "🎉 You Win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You Win!"
            elif player == computer:
                tie_game += 1
                return "🐱‍👤Tie Game!"

            else:
                computer_wins += 1
                return "😒 Computer Wins"

        game_result = decide_winner(player, computer)

        print(game_result)
        nonlocal game_count
        game_count += 1
        print(f"\nGame Count: {str(game_count)}")
        print(f"\nPlayer Wins: {str(player_wins)}")
        print(f"\nComputer Wins: {str(computer_wins)}")
        print(f"\nTie Games: {str(tie_game)}")

        print("\nPlay Again?")

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
            sys.exit("Byeeeee! ❤")

    return play_rps


play = rps()

play()
