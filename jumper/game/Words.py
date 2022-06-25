# Global Imports:
import random

'''This is a list of words that the program will choose from. We went to a random word 
generator and generated 15 random words to get these.'''

class RandomWord:
    """This is a class that creates a list of words that the program will choose from"""
    def __init__(self):
        self._words_list = []
    
    def _get_random_word(self):
        self._words_list = ["apricot","grounds","analyst","magnetic","desire","foster",
                            "aquisition","provoke","reserve","confront","helpless",
                            "decline","bargain","injection","monopoly"]
        word = random.choice(self.words_list).upper()
        return word
