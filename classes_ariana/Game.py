import random
from classes_ariana.Words import words

class Game:

    def __init__(self):
        self.word = words
        self.guess = ""
        self.reveal = list(len(self.word)*'_')
        
        self.won = False
        self.lose = False
        self.lives = 4

    def letter_check(self, letter):

        for i in range(0, len(self.word)):
            letter = self.word[i]
            if self.guess == letter:
                self.reveal[i] = self.guess
        if '_' not in self.reveal:
            return True
        else:
            return False