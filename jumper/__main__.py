# Global Imports:
from game.director import _Director

def __main__():
    """Calls the director class to play the game"""
    director = _Director()
    director._start_game()

# calls the main function to play the game
if __name__ == '__main__':
    __main__()