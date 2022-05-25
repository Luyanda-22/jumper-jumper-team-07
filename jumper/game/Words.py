import random

'''This is a list of words that the program will choose from. I went to a random word 
generator and generated 15 random words to get these.'''


#for some reason, the code would only run if I took it out of the class and had it be its own stray function.
words_list = ["apricot", "grounds", "analyst", "magnetic", "desire", "foster", 
"aquisition", "provoke", "reserve", "confront", "helpless", "decline", "bargain", 
"injection", "monopoly"]

words = random.choice(words_list).upper()

'''def get_random_word(self):
    """PUT COMMENT HERE"""
    # choose a random word
    words = random.choice(self.words_list).lower()
    # split word into a list
    split_word = list(words)
    return split_word'''