class Point:
    """Any distance from a relative origin (0, 0)."""

    #The responsibility of Point is to hold and provide information 
    # about itself. Point has a few convenience methods for adding, 
    # scaling, and comparing them.
    """
    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.
    """
    
    def __init__(self, x, y):
        # This Constructs a new Point using the specified 
        # x and y values.
        """
        Args:
            x (int): The specified x value.
            y (int): The specified y value.
        """
        self._x = x
        self._y = y

    def add(self, other):
        # This gets a new point that is the sum of this 
        # and the given one.
        """
        Args:
            other (Point): The Point to add.

        Returns:
            Point: A new Point that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        # This checks whether or not this Point is equal 
        # to the given one.
        """
        Args:
            other (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        # This gets the horizontal distance.
        """
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        # This gets the vertical distance.
        """
        Returns:
            integer: The vertical distance.
        """
        return self._y

    def reverse(self):
        # This reverses the point by inverting both x and y values.
        """
        Returns:
            Point: A new point that is reversed.
        """
        new_x = self._x * -1
        new_y = self._y * -1
        return Point(new_x, new_y)

    def scale(self, factor):
        # This scales the point by the provided factor.
        """
        Args:
            factor (int): The amount to scale.
            
        Returns:
            Point: A new Point that is scaled.
        """
        return Point(self._x * factor, self._y * factor)