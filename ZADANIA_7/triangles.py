#!usr/bin/env python3
# -*- coding: utf -8-*-
import sys
sys.path.insert(0, "../ZADANIA_6")
from point import *

def wspolliniowe(x1, y1, x2, y2, x3, y3):
    if(x1 == x2):
        if(x2 == x3):
            return True
        return False
    a = (y1 - y2) /(x1 - x2)
    b = y1 - a*x1
    return y3 == (a* x3 + b)

def srodekodcinka(x1, y1, x2, y2):
    return Point((x1+x2)/2 , (y1+y2)/2)

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3): # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        """ Funkcja tworząca trójkąt z trzech niewspółliniowych punktów
        >>> Triangle(0, 1, 0, 2, 0, 3)
        Traceback (most recent call last):
            ...
        ValueError: Punkty współliniowe!
        >>> Triangle(0, 1, 1, 1, 1, 3)
        Triangle(0, 1, 1, 1, 1, 3)
        """
        if wspolliniowe(x1, y1, x2, y2, x3, y3):
            raise ValueError("Punkty współliniowe!")
         
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)


    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return '['+str(self.pt1) + ", " + str(self.pt2) + ", " + str(self.pt3) + ']'
    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return f'Triangle({ self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})' 
    
    def __eq__(self, other):   # obsługa tr1 == tr2
        """ Funkcja zwracająca czy dane trójkąty są te same
        >>> Triangle(1, 2, 2, 3, 1, 4) == Triangle(1, 2, 2, 3, 7, 4)
        False
        >>> Triangle(1, 2, 2, 3, 8, 4) == Triangle(2, 3, 1, 2, 8, 4)
        True
        >>> Triangle(1, 2, 2, 3, 3, 4) == Triangle(1, 2, 2, 3, 3, 4)
        Traceback (most recent call last):
            ...
        ValueError: Punkty współliniowe!
        """
        if(isinstance(other, Triangle)):
            return (self.pt1 == other.pt1 or self.pt1 == other.pt2 or self.pt1 == other.pt3) and (self.pt2 == other.pt1 or self.pt2 == other.pt2 or self.pt2 == other.pt3) and (self.pt3 == other.pt1 or self.pt3 == other.pt2 or self.pt3 == other.pt3)
        return False

    def __ne__(self, other):        # obsługa tr1 != tr2
        """ Funkcja zwracająca czy dane trójkąty są te same
        >>> Triangle(1, 2, 2, 3, 1, 4) != Triangle(1, 2, 2, 3, 7, 4)
        True
        >>> Triangle(1, 2, 2, 3, 8, 4) != Triangle(2, 3, 1, 2, 8, 4)
        False
        >>> Triangle(1, 2, 2, 3, 3, 4) != Triangle(1, 2, 2, 3, 3, 4)
        Traceback (most recent call last):
            ...
        ValueError: Punkty współliniowe!
        """
        return not self == other

    def center(self):          # zwraca środek trójkąta
        return Point((self.pt1.x+self.pt2.x+self.pt3.x)/3, (self.pt1.y+self.pt2.y+self.pt3.y)/3)

    def area(self):            # pole powierzchni
        return 0.5*(self.pt1.x * self.pt2.y + self.pt2.x*self.pt3.y + self.pt3.x*self.pt1.y - self.pt3.x *self.pt2.y - self.pt1.x*self.pt3.y -self.pt2.x* self.pt1.y)

    def move(self, x, y):      # przesunięcie o (x, y)
        """ Funkcja zwracająca trójkąt przesunięty o (x, y)
        >>> Triangle(0, 1, 0, 3, 1, 2).move(1, 2)
        Triangle(1, 3, 1, 5, 2, 4)
        >>> Triangle(0, 1, 0, 3, 1, 2).move('a', 7)
        Traceback (most recent call last):
            ...
        TypeError: To zły typ!
        """
        if(isinstance(x, (int, float)) and isinstance(y, (int, float))):
            self.pt1.x += x
            self.pt2.x += x
            self.pt3.x += x

            self.pt1.y += y
            self.pt2.y += y
            self.pt3.y += y
            return self
        
        raise TypeError("To zły typ!")

    def make4(self):           # zwraca listę czterech mniejszych
        Point1 = srodekodcinka(self.pt1, self.pt2)
        Point2 = srodekodcinka(self.pt2, self.pt3)
        Point3 = srodekodcinka(self.pt3, self.pt1)

        Triangle1 = Triangle(self.pt1, Point1, Point3)
        Triangle2 = Triangle(self.pt2, Point1, Point2)
        Triangle3 = Triangle(self.pt3, Point3, Point2)
        Triangle4 = Triangle(Point1, Point2, Point3)

        return [Triangle1, Triangle2, Triangle3, Triangle4]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
