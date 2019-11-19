class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        """ Funkcja zwraca string "(x, y)"
	>>> str(Point(0, 0))
        '(0, 0)'
        >>> str(Point(7, 42))
        '(7, 42)'
        >>> str(Point(0.0, 0.0))
        '(0.0, 0.0)'
        """
        return "("+ str(self.x) + ", "+ str(self.y) + ")"

    def __repr__(self):        # zwraca string "Point(x, y)"
        """ Funkcja zwraca string "Point(x, y)"
        >>> repr(Point(0, 0))
        'Point(0, 0)'
        >>> repr(Point(7, 42))
        'Point(7, 42)'
        >>> repr(Point(0.0, 0.0))
        'Point(0.0, 0.0)'
        """
        return "Point("+ str(self.x) + ", "+ str(self.y) + ")"
    
    def __eq__(self, other):   # obsługa point1 == point2
        """ Funkcja zwraca informację, czy point1 == point2
        >>> Point(0, 0) == Point(0, 0)
        True
        >>> Point(0.0, 0.0) == Point(0, 0)
        True
        >>> Point(1, 2) == Point(1, 2)
        True
        >>> Point(1, 1) == Point(1, 2)
        False
        >>> Point(2, 1) == Point(1, 1)
        False
        >>> Point(2, 1) == Point(1, 2)
        False
        """
        return (self.x == other.x and self.y == other.y)
    
    def __ne__(self, other):   # obsługa point1 != point2
        """ Funkcja zwraca informację, czy point1 != point2
        >>> Point(0, 0) != Point(0, 0)
        False
        >>> Point(0.0, 0.0) != Point(0, 0)
        False
        >>> Point(1, 2) != Point(1, 2)
        False
        >>> Point(1, 1) != Point(1, 2)
        True
        >>> Point(2, 1) != Point(1, 1)
        True
        >>> Point(2, 1) != Point(1, 2)
        True
        """
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        """ Funkcja zwraca sumę v1 + v2
        >>> Point(0, 0) + Point(0, 0)
        Point(0, 0)
        >>> Point(1, 0) + Point(0, 0)
        Point(1, 0)
        >>> Point(0, 1) + Point(0, 0)
        Point(0, 1)
        >>> Point(1, 1) + Point(0, 0)
        Point(1, 1)
        >>> Point(-1, -1) + Point(1, 1)
        Point(0, 0)
        """
        return Point(self.x + other.x, self.y + other.y) 
    
    def __sub__(self, other):  # v1 - v2
        """ Funkcja zwraca różnicę v1 - v2
        >>> Point(0, 0) - Point(0, 0)
        Point(0, 0)
        >>> Point(2, 2) - Point(1, 1)
        Point(1, 1)
        >>> Point(1, 1) - Point(-1, -1)
        Point(2, 2)
        """
        return Point(self.x - other.x, self.y - other.y) 
    
    def __mul__(self, other): # v1 * v2, iloczyn skalarny
        """ Funkcja zwraca iloczyn skalarny v1* v2
        >>> Point(1, 2) * Point(2, 1)
        4
        >>> Point(2, 4) * Point(2, 4)
        20
        """
        return self.x * other.x + self.y * other.y 
    
    def cross(self, other):   # v1 x v2, iloczyn wektorowy 2D
        """ Funkcja zwraca iloczyn wektorowy v1 x v2
        >>> Point(1, 0).cross(Point(0, 1))
        1
        >>> Point(1, 2).cross(Point(1, 2))
        0
        >>> Point(1, 0).cross(Point(1, 0))
        0
        """
        return self.x * other.y - self.y * other.x

    def length(self):   # długość wektora
        """ Funkcja zwraca długość wektora
        >>> Point(0, 0).length()
        0.0
        >>> Point(1, 0).length()
        1.0
        >>> Point(0, 1).length()
        1.0
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5 

if __name__ == '__main__':
    # Kod testujący moduł.
    import doctest
    doctest.testmod()
