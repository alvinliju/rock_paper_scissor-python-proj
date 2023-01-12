import random


def get_choices():
  player_choice = input("enter a choice (rock, paper, sissors: ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_win(player, computer):
  print(f"you choose {player},  computer chose {computer}")
  if player == computer:
    return "its a tie"
  elif player == "rock":
    if computer == "scissors":
      return "you win lol"

    else:
      return "you lose"

  elif player == "paper":
    if computer == "rock":
      return "you win"
    else:
      return "you loose"

  elif player == "scissors":
    if computer == "paper":
      return "you win lol"

    else:
      return "you lose"


while True:
    choices = get_choices()
    if choices["player"] == "stop":
        break
    result = check_win(choices["player"], choices["computer"])
    print(result)