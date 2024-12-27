import sys
import random
from enum import Enum


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    print("")
    playerchoice = input(
        '\nEnter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n')
    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps

    player = int(playerchoice)

    computer_choice = random.choice("123")

    computer = int(computer_choice)

    print("\nYou chose " + playerchoice + " for " +
          str(RPS(player)).replace('RPS.', '') + ".")
    print('Computer chose ' + str(RPS(computer)).replace('RPS.', '') + ".")
    print('')

    if player == 1 and computer == 3:
        print("🎉 You Win! ")
    elif player == 2 and computer == 1:
        print("🎉 You Win!")
    elif player == 3 and computer == 2:
        print("🎉 You Win!")
    elif player == computer:
        print("🐱‍👤Tie Game!")
    else:
        print("😒 Computer Wins")

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


play_rps()
