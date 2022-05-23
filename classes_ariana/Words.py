import random


'''This is a list of words that the program will choose from. I went to a random word 
generator and generated 15 random words to get these.'''

list = ["apricot", "grounds", "analyst", "magnetic", "desire", "foster", 
"aquisition", "provoke", "reserve", "confront", "helpless", "decline", "bargain", 
"injection", "monopoly"]

words = random.choice(list).lower()

#print(words)