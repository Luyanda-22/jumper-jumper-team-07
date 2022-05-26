# DELETE ALL DEBUGGING LINES WHEN THE PROGRAM IS FINISHED
from game.Words import words
from game.Guy import guy

class Jumper:
    """This is the part that runs the game "Jumper."""
    def __init__(self):
        """These are attributes to the Jumper game"""
        # variables for the random word
        self.word = words
        self.guess = ""
        self.reveal = list((len(self.word)*'_'))

        # variables for win or lose
        self.won = False
        self.lose = False
        self.lives = 4

    def letter_check(self, letter, word):
        """Asks the user to guess a letter, then checks if the user was correct or not. If correct, then reveal a letter"""

        """# DEBUGGING - PRINT THE RANDOM WORD
        print(self.split_word)
        # print the blank word
        print(*self.reveal, sep= ' ')
        # prints the jumper
        self.jumper_class.print_jumper()
        #DEBUGGING - GUESS A LETTER
        self.guess = input('Guess a letter: ')"""

        for i in range(0, len(self.word)):
            letter = self.word[i]
            if self.guess == letter:
                self.reveal[i] = self.guess
        if '_' not in self.reveal:
            return True
        else:
            return False

    def process(self):
        """This is the logic of the game"""
        while self.won == False and self.lives > 0:
            self.show()
            self.guess = input("Guess a letter! ")
            self.guess = self.guess.upper()
            
            if self.guess == self.word:
                self.won = True
                self.reveal = self.word
            if len(self.guess) == 1 and self.guess in self.word:
                self.won = self.letter_check(self.guess, self.word)

                """Win Lose display"""
                if self.won == True:
                    print(f"Good job, you guessed the word {self.word}.")
                else: 
                    print("Good job! That letter IS in the word!")
            else:
                self.lives-=1

        #This prints game over
            if self.lives == 0:
                self.lose = True

            if self.lose == True:
                print(guy[4])
                print('You did not save the Jumper...')
                self.lost = False
                print(self.word)

    def show(self):
        """This displays the guy from the Guy class"""
        print(guy[4 - self.lives])
        print(self.reveal)

        if self.lives > 0:
            print(f"You have {self.lives} live(s) left...")
        else:
            print("Game over")


