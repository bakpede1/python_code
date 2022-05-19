rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random 

# initialize constants
GAME_IMAGES = [rock, paper, scissors]
WIN_MSG = "You win!"
LOSE_MSG = "You lose"
DRAW_MSG = "It's a draw"

choice = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors\n"))

# input validator
if choice > 3 or choice < 0:
  print("You typed an invalid number you lose.")
	
else:
  print(GAME_IMAGES[choice])

  comp_choice = random.randint(0,2)

  print("Computer chose:")
  print(GAME_IMAGES[comp_choice])
  
  if choice == 0 and comp_choice == 2:
    print(WIN_MSG)
  elif comp_choice == 0 and choice == 2:
    print(LOSE_MSG)
  elif choice > comp_choice:
    print(WIN_MSG)
  elif comp_choice > choice:
    print(LOSE_MSG)
  elif choice == comp_choice:
    print(DRAW_MSG)
