class Point:
    """A distance from a relative origin (0, 0).

    The responsibility of Point is to hold and provide information about itself. Point has a few 
    convenience methods for adding, scaling, and comparing them.

    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.
    """

    def __init__(self, x, y):
        """Constructs an instance of Point."""
        self._x = x
        self._y = y

    def get_x(self):
        """Returns the x-coordinate of the point
        Returns: 
            self._x: The x-coordinate
        """
        return self._x

    def get_y(self):
        """Returns the y-coordinate of the point
        Returns: 
            self._y: The y-coordinate
        """
        return self._y

    def add(self, other):
        """Adds the coordinates of two points together resulting in 
        a point further away
        Args:
            other (Point): The Point to compare

        Returns:
            Point: a new point that is the sum
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x,y)

    def equals(self, other):
        """Compares two points for equality.
        Args:
            other (Point): The Point to compare

        Returns:
            boolean: True if equal; False if not
        """
        if self._x == other.get_x() and self._y == other.get_y():
            return True
        else:
            return False
        
    def reverse(self):
        """Reverses the point by inverting both x and y values.

        Returns:
            Point: A new point that is reversed.
        """
        new_x = self._x * -1
        new_y = self._y * -1
        return Point(new_x, new_y)

    def scale(self, factor):
        """
        Scales the point by the provided factor.

        Args:
            factor (int): The amount to scale.
            
        Returns:
            Point: A new Point that is scaled.
        """
        return Point(self._x * factor, self._y * factor)