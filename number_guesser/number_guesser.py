import random

# Have the computer select a random number 1 -100
# The user will guess the number. 
# The computer will print out if the guess is too high or too low.
# Allow as many guess until the user gets it right. 
# Print out how many guesses it took. 
# **Have the user change the range of what they were guessing.**
# **Put methods into a 'NumberGuesser' class.**
# **Write a reset behavior, so the user can play the game again if they want**

class NumberGuesser:
    def __init__(self):
        self.upper_limit = self.set_limit("upper")
        self.lower_limit = self.set_limit("lower")
        self.number_of_guesses = 1
        self.number = self.set_secret_number()
        self.guess = self.get_first_guess()
    
    def get_first_guess(self):
        return int(input(f'Could you please guess a number between {self.lower_limit} and {self.upper_limit}: '))

    def get_guesses(self):
        while self.guess != self.number:
            self.number_of_guesses += 1
            if self.guess > self.number:
                self.guess = int(input('Your guess was too high, could you please guess agian?: '))
            elif self.guess < self.number:
                self.guess = int(input('Your guess was too low, could you please guess agian?: '))

        print("You guess the correct number!")
        print("Guesses to complete the game: " + str(self.number_of_guesses))

    def set_secret_number(self):
        return random.randint(self.lower_limit, self.upper_limit)

    def set_limit(self, limit):
        return int(input(f"Please set the {limit} guess limit to the game: "))

    def reset(self):
        self.upper_limit = self.set_limit("upper")
        self.lower_limit = self.set_limit("lower")
        self.number_of_guesses = 1
        self.number = self.set_secret_number()
        self.guess = self.get_first_guess()

    
number_guesser = NumberGuesser()
number_guesser.get_guesses()
number_guesser.reset()
number_guesser.get_guesses()