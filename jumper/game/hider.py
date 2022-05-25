import random
class Hider_word:
    def __init__(self):
        self.words = ["apricot", "grounds", "analyst", "magnetic", "desire", "foster", 
                     "aquisition", "provoke", "reserve", "confront", "helpless", "decline", "bargain", 
                     "injection", "monopoly"]
        self._secrete_word = ''
        self._guesses = ''
        self._num_wrong_guesses = 0
        self._chosen_letters = []


    def random_word(self):
        self._secrete_word = random.choice(self.words)
        self._guesses = '_ ' * len(self._secrete_word)

        return self._secrete_word

    def checking_guess(self, letter):
        
        #Converting the word to a list to check every characater
        temp_list = list(self._secrete_word)

        for i, c in enumerate(self._secrete_word):
            if letter == c:
                temp_list[i] = c
        self._guesses = "".join(temp_list)

        #if the user answer incorrectly we will ad a point to num wrong guesses
        if letter not in self._secrete_word:
            self._num_wrong_guesses +=1

    def add_letter(self, letter):
        
        #This adds the letter to the array that will keep track on the letter that the user guesses.
        self._chosen_letters.append(letter)

    def get_chosen_letters(self):

        return self._chosen_letters
    
    def get_num_wrong_guesses(self):

        return self._num_wrong_guesses

    def get_guesses(self):
        return self._guesses

    def guess_correctly(self):
        return self._secrete_word == self._guesses 
    

