import constants, pyray
from game.shared.point import Point

class Actor():
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
        _width (int): The width of the shape.
        _height (int): The height of the shape.
        _color (Color): The color of the text.
        _type (str): The type of shape.
    """

    def __init__(self):
        """Constructs an instance of Actor"""
        self._position = Point(0,0)
        self._velocity = Point(0,0)
        self._width = constants.CELL_SIZE
        self._height = constants.CELL_SIZE
        self._color = pyray.DARKGRAY
        self._type = "rect"

    def set_position(self, position):
        """Set the position of Actor
        Args:
            position (Point): An instance of Point
        """
        self._position = position
    
    def set_velocity(self, velocity):
        """Set the velocity of Actor
        Args:
            velocity (Point): An instance of Point
        """
        self._velocity = velocity

    def set_width(self, width):
        """Set the width of Actor
        Args:
            width (int): The desired width for Actor
        """
        self._width = width

    def set_height(self, height):
        """Set the height of Actor
        Args:
            height (int): The desired height for Actor
        """
        self._height = height
    
    def set_color(self, color):
        """Set the color of Actor
        Args:
            color (Color): A pyray default color
        """
        self._color = color

    def set_type(self, type):
        """Set the type of shape
        Args:
            type (str): The desired shape
        """
        self._type = type

    def move_next(self):
        """Move the actor to the next position"""
        x = (self._position.get_x() + self._velocity.get_x())
        y = (self._position.get_y() + self._velocity.get_y())

        self._position = Point(x, y)

    def get_position(self):
        """Get the position of Actor
        Return:
            position (Point): An instance of Point
        """
        return self._position

    def get_velocity(self):
        """Get the velocity of Actor
        Return:
            velocity (Point): An instance of Point
        """
        return self._velocity

    def get_width(self):
        """Get the width of Actor
        Return:
            width (int): The width of Actor
        """
        return self._width

    def get_height(self):
        """Get the height of Actor
        Return:
            height (int): The height of Actor
        """
        return self._height
    
    def get_color(self):
        """Get the color of Actor
        Return:
            color (Color): A pyray default color
        """
        return self._color

    def get_type(self):
        """Get the type of shape
        Return:
            type (str): The type of shape
        """
        return self._type