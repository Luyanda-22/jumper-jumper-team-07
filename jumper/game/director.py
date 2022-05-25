from msilib.schema import SelfReg
from game.terminal_service import TerminalService
from game.hider import Hider_word
from game.jumper import Jumper

"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/encapsulation/materials/jumper-specification.html
"""


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: For getting and displaying information on the terminal.
    """
    

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._letter = ''
        self._hider = Hider_word()
        self._user_player = Jumper()
        self._terminal_service = TerminalService()

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        self._hider.random_word()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Update this comment

        Args:
            self (Director): An instance of Director.
        """
        self._letter = self._terminal_service.read_text('Guess a letter [a - z]: ')

    def _do_updates(self):
        """Update this comment

        Args:
            self (Director): An instance of Director.
        """
        self._hider.checking_guess(self._letter)
        self._hider.add_letter(self._letter)
        

    def _do_outputs(self):
        """Update this comment

        Args:
            self (Director): An instance of Director.
        """
        pass
