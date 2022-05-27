import constants, pyray 
from game.casting.actor import Actor

class Message(Actor):
    """A visible text for display to the screen.

    The responsibility of Message is to keep track of the position,
    text, font_size, and color in 2D space.

    Attributes:
        text (string): The text to display
        font_size (int): The font size to use.
        color (Color): The color of the text.
        position (Point): The screen coordinates.
        """

    def __init__(self):
        """Constructs a new instance of Message"""
        self._text = ""
        self._font_size = constants.FONT_SIZE
        self._color = pyray.WHITE 

    def set_text(self, text):
        """Set the text to the given one.
        Args:
            text (str): The given text
        """
        self._text = text

    def set_font_size(self, font_size):
        """Set the font size to the given one.
        Args:
            font_size (int): A given font size
        """
        self._font_size = font_size

    def set_color(self, color):
        """Set the color to the given one.
        Args:
            color (Color): A pyray color object
        """
        self._color = color

    def get_text(self):
        """Get the text to the given one.
        Return:
            text (str): The given text
        """
        return self._text

    def get_font_size(self):
        """Get the font size to the given one.
        Return:
            font_size (int): A given font size
        """
        return self._font_size

    def get_color(self):
        """Get the color to the given one.
        Return:
            color (Color): A pyray color object
        """
        return self._color
