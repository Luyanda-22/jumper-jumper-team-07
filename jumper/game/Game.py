# Global Imports:
from game.Words import _RandomWord
from game.Jumper import _Jumper
from game.terminal_service import TerminalService

class _Game:
    """This is the part that runs the game Jumper.
    
    Args are explained in the __init__ method below
    """
    def __init__(self):
        """These are attributes to the Jumper game"""
        # variables for the random word
        self.word = _RandomWord._get_random_word(self)
        self.guess = ""
        self.reveal = list((len(self.word)*'_'))
        self.guy = _Jumper()
        self.terminal_service = TerminalService()
        # variables for win or lose
        self.won = False
        self.lose = False
        self.lives = 4

    def letter_check(self, letter, word):
        """Check if the user's letter guess was correct or not. If correct, then reveal a letter"""

        """# DEBUGGING - PRINT THE RANDOM WORD
        print(self.split_word)
        # print the blank word
        print(*self.reveal, sep= ' ')
        # prints the jumper
        self.jumper_class.print_jumper()
        #DEBUGGING - GUESS A LETTER
        self.guess = self.terminal_service.get_input('Guess a letter: ')"""

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
            self.guess = self.terminal_service.get_input("Guess a letter! ")
            self.guess = self.guess.upper()
            
            if self.guess == self.word:
                self.won = True
                self.reveal = self.word
            if len(self.guess) == 1 and self.guess in self.word:
                self.won = self.letter_check(self.guess, self.word)

                """Win Lose display"""
                if self.won == True:
                    self.terminal_service.show_text(f"Good job! You guessed the word {self.word}!")
                    # this ends the game
                    print()
                    exit()
                else: 
                    self.terminal_service.show_text(f'Good job! The letter "{self.guess}" is in the word!')
            else:
                self.lives-=1

        #This prints game over
            if self.lives == 0:
                self.lose = True

            if self.lose == True:
                self.terminal_service.show_text(self.guy.guy[4])
                self.terminal_service.show_text('You did not save the Jumper...')
                self.lost = False
                self.terminal_service.show_text(f'The word was: {self.word}')
                # this ends the game
                print()
                exit()

    def show(self):
        """This displays the guy from the Guy class & shows how many lives are left"""
        self.terminal_service.show_text(self.guy.guy[4 - self.lives])
        # print the blank word
        # the following print statement does not use terminal_service.show_text because show_text does not accept sep= ' '
        print(*self.reveal, sep= ' ')
        print()

        if self.lives > 0:
            self.terminal_service.show_text(f"You have {self.lives} live(s) left...")
        else:
            self.terminal_service.show_text("Game over")


