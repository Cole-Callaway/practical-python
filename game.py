import random
player = input('howdy, whats your name?\n')
print(player,'im thinking of a number between 1 and 100')



class NumberGuessingGame:

    def __init__(self):
        
        self.LOWER = 1
        self.HIGHER = 100

    
    def get_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)

   
    def start(self):
        
        random_number = self.get_random_number()

        print(
            "Try and guess the number")

        
        chances = 0
        while True:
            user_number = int(input("Your Guess? "))
            if user_number == random_number:
                print(
                    f"Well done, {player} You got it in {chances + 1} step{'s' if chances > 1 else ''}!")
                break
            elif user_number < random_number:
                print("guess is too low, try again")
            else:
                print("guess is too high, try again")
            chances += 1


numberGuessingGame = NumberGuessingGame()
numberGuessingGame.start()