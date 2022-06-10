import random

computer_choice = random.choice(['scissors', 'rock', 'paper'])

user_choice = input("Do you want to - rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print("TIE")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('win, the computer had ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('win, the computer had ' + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('win, the computer had ' + computer_choice)
else:
    print('YOU LOSE, the computer had ' + computer_choice)