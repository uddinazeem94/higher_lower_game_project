# Higher Lower Game Project
from art import main_logo, vs_logo, celebrities
from replit import clear
import random

#function for random choice from list
def random_choice():
  return random.choice(list((celebrities)))

# Looping as a function if user wants to restart
def higher_lower():

  clear()

  # Welcome message
  print(" Welcome... Try out the higher/lower game.")
  print(main_logo)

  # Looping through the list of celebrities
  score = 0
  game_over = False
  option_a = random_choice()
  value_a = celebrities[option_a]

  # Keeping the previous celebrity to compare with another one
  while game_over is not True:
    option_b = random_choice()

    # Generating a random choice if both options are same
    while option_b == option_a:
      option_b = random_choice()

    value_b = celebrities[option_b]
    print(f"Your Score is {score}\n")
    print(f"Option A- {option_a}")
    print(vs_logo)
    print(f"Option B- {option_b}\nWho has more followers on InstaGram?\n")
    answer = input("type 'a' or 'b'\n").lower()
    if answer == 'a' and value_a > value_b:
      score += 1
      option_a = option_b
      value_a = value_b
      clear()

    elif answer == 'b' and value_b > value_a:
      score +=1
      option_a = option_b
      value_a = value_b
      clear()

    else:
      print(f"Wrong Answer. Your Score is: {score}\n")
      game_over = True


  run_again = input("Do you want to play again?")
  if run_again == 'yes' or run_again == 'y':
    higher_lower()

  else:
    exit()
higher_lower()
