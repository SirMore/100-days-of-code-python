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

# Importing the random module to help in the generation of random numbers
import random 

# Asking the user to make his/her choice and printing out to the screen
user_choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
print("You chose:")
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Sorry!! The choice is different from the allowed integer choices")

# generating a random choice for the computer and printing the choice on the screen
computer_choice = random.randint(0,2)
print("Computer chose:")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

'''
Following the rules of the game:
---- Rock wins against scissors
---- Scissors win against paper
---- Paper wins against rock
'''

if user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
else:
    print("You lose!")
#print(computer_choice)
