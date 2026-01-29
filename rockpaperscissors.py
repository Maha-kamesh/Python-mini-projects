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
game_img=[rock,paper,scissors]
option=int(input("What do you choose?Type 0 for Rock, 1 for Paper or 2 for scissors"))
if option>=0 and option<=2:
    print(game_img[option])
computer_choice=random.randint(0,2)
print("Computer chose: ")
print(game_img[computer_choice])
if option>=3 or option<=0:
    print("Invalid option")
elif option==0 and computer_choice==2:
    print("You win")
elif option==2 and computer_choice==0:
    print("You lose")
elif option>computer_choice:
    print("You win")
elif computer_choice>option:
    print("you lose")
elif computer_choice==option:
    print("Draw!")

else:
    print("Invalid option")

