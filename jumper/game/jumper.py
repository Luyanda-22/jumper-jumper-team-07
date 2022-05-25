
class Jumper:
    def __init__(self):
        self._num_wrong_guesses = 0
        self.max_chances = 5
        self._jumper = [
    '   ___',
    '  /   \\',
    '  -----',
    '  \\   /',
    '   \\ /',
    '    0',
    '   /|\\',
    '   / \\',
    '',
    '^^^^^^^^^'
    ]

    def get_jumper(self):
        return self._jumper

    def chaging_parachute(self, incorrect_guess):
        if incorrect_guess == self.max_chances:
            self._jumper[0] = " X "
        elif self._num_wrong_guesses != incorrect_guess:
            self._jumper.pop(0)
        
    def lost(self):
        # Returning if the user ran out of lives
        return self._num_wrong_guesses == self.max_chances