import random 
roll = random.randint(1, 6)

guess = int(input('Guess the dice roll:\n'))

if guess == roll:
    print ("correct the rolled a " + str(roll))
else:
    print("wrong the rolled a " + str(roll))