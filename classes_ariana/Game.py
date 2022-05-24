# DELETE ALL DEBUGGING LINES WHEN THE PROGRAM IS FINISHED
from Words import RandomWord
from Guy import Jumper

class Game:
    """PUT COMMENT HERE"""
    def __init__(self):
        """PUT COMMENT HERE"""
        # variables for the random word
        self.random_word = RandomWord()
        self.split_word = self.random_word.get_random_word()
        # SELF.GUESS WILL BE USED IN THE DIRECTOR CLASS TO GET THE USER INPUT
        # self.guess = letter_guess
        self.reveal = list((len(self.split_word)*'_'))

        # variables for the jumper
        self.jumper_class = Jumper()
        self.jumper_list = self.jumper_class.jumper
        self.print_jumper = self.jumper_class.print_jumper

        # variables for win or lose
        self.won = ''
        self.lose = ''

    def letter_check(self):
        """Asks the user to guess a letter, then checks if the user was correct or not. If correct, then reveal a letter"""

        # DEBUGGING - PRINT THE RANDOM WORD
        print(self.split_word)
        # print the blank word
        print(*self.reveal, sep= ' ')
        # prints the jumper
        self.jumper_class.print_jumper()
        #DEBUGGING - GUESS A LETTER
        self.guess = input('Guess a letter: ')

        # VALIDATION SECTION
        if self.guess in self.split_word:
            # checks if the user was correct and reveal a letter if so.
            for i in self.split_word:
                # letter = self.split_word[i]
                # if the user is correct, reveal that letter in its place
                if self.guess == i:
                    letter_index = self.split_word.index(self.guess)
                    self.reveal[letter_index] = self.guess
                    # FIX THIS!!! THIS ONLY CHANGES THE FIRST INSTANCE OF THE LETTER, NO OTHER INSTANCES
            print(self.reveal)
            # if the user guesses all of the letters correctly, return True
            if '_' not in self.reveal:
                return self.won == True
            # if the user has not guessed all of the letters yet, return False
            else:
                return False
        elif self.guess not in self.split_word:
            print('You guessed wrong!')
            # when the user guesses wrong, remove the current first line from the list & print the remaining guess list
            self.jumper_class.remove_line
            # if index 0 in the jumper list == '    O' then change the head to X & end the game
            if self.jumper_list[0] == '    O':
                self.jumper_list[0] = '    X'
            # game over & end the game
            print('Game over! You did not save the Jumper')
            # returns self.lose == False so we can end the game in the director file
            return self.lose == False


game = Game()
game.letter_check()