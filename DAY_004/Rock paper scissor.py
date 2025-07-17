import random

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
choice_images = [rock,paper,scissors]
player_choice = int(input("Plese enter 0 for rock , 1 for paper and 2 for scissors\n"))
if player_choice >= 0 or player_choice < 3:
    print(choice_images[player_choice])
computer_choice = random.randint(0,2)
print( "computer choosed")
print(choice_images[computer_choice])

if player_choice < 0 or player_choice >2:
    print("Invalid input !! U losse")
elif player_choice == 0 and computer_choice == 2:
    print("U win")
elif computer_choice == 0 and player_choice == 2:
    print("U lose")
elif player_choice > computer_choice:
    print("player wins")
elif computer_choice> player_choice:
    print("computer wins")
elif computer_choice == player_choice:
    print("draw")
