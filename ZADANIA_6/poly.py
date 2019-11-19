#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys
sys.path.insert(0, "../ZADANIA_5")
from polys import *


class Poly:
    """Klasa reprezentująca wielomiany."""

    # wg Sedgewicka - tworzymy wielomian c*x^n
    def __init__(self, c=0, n=0):
        if isinstance(c, (tuple, list)):
            self.a = list(c)
            self.size = len(self.a)
            return
        self.size = n + 1
        self.a = self.size * [0]
        self.a[self.size-1] = c
    
    def __repr__(self):
        """
        >>> repr(Poly(1, 2))
        'Poly([0, 0, 1])'
        >>> repr(Poly(1, 1))
        'Poly([0, 1])'
        >>> repr(Poly(1, 0))
        'Poly([1])'"""
        return f'Poly({self.a})'

    def __str__(self):
        """ Funkcja zwracająca listę współczynników wielomianu
        >>> str(Poly(1, 2))
        '[0, 0, 1]'
        >>> str(Poly(1, 1))
        '[0, 1]'
        >>> str(Poly(1, 0))
        '[1]'"""
        return str(self.a)
    
    def __add__(self, other):  # poly1 + poly2
        """ Funkcja zwracająca sumę wielomianów 
        >>> Poly(1, 2) + Poly(1, 3)
        Poly([0, 0, 1, 1])
        >>> Poly([1, 2]) + Poly([3, 4])
        Poly([4, 6])
        >>> Poly([1]) + Poly([0, 1])
        Poly([1, 1])
        >>> Poly([1, 2]) + Poly([0, 0, 3, 4])
        Poly([1, 2, 3, 4])
        >>> Poly([1, 2]) + Poly([-1, -2])
        Poly([0, 0])
        """
        return Poly(add_poly(self.a, other.a))
    
    def __sub__(self, other):  # poly1 - poly2
        """ Funkcja zwracająca różnicę wielomianów 
        >>> Poly([2]) - Poly([1])
        Poly([1])
        >>> Poly([2, 3]) - Poly([1, 2])
        Poly([1, 1])
        >>> Poly([1, 2, 3]) - Poly([1, 2, 3])
        Poly([0, 0, 0])
        """
        return (self + -(other))

    def __mul__(self, other):  # poly1 * poly2
        """ Funkcja zwracająca iloczyn wielomianów
	>>> mul_poly([0, 0, 1], [1, 2])
        [0, 0, 1, 2]
	>>> mul_poly([1, 2], [4, 6])
	[4, 14, 12]
	>>> mul_poly([1, 2], [0])
    	[0]
    	>>> mul_poly([1, 2, 3], [2])
	[2, 4, 6]
	>>> mul_poly([2], [1, 2, 3])
	[2, 4, 6]"""
        return Poly(mul_poly(self.a, other.a))

    def __pos__(self):         # +poly1 = (+1)*poly1
        """ Funkcja zwracająca samą siebie
        >>> +Poly([1])
        Poly([1])
        """
        return self

    def __neg__(self):         # -poly1 = (-1)*poly1
        """ Funkcja zwracająca swoją negację
        >>> -Poly([1])
        Poly([-1])
        >>> -Poly([1, 2])
        Poly([-1, -2])
        >>> -Poly([0])
        Poly([0])
        >>> -Poly([0, 0, 0])
        Poly([0, 0, 0])
	"""
        return Poly([-a for a in self.a])

    def __eq__(self, other):   # obsługa poly1 == poly2
        """ Funkcja zwracająca informację czy dwa wielomiany są sobie równe
        >>> Poly([1]) == Poly([1])
	True
	>>> Poly([1, 2]) == Poly([1, 2])
	True
	>>> Poly([0]) == Poly([0])
	True
    	>>> Poly([0, 0, 0]) == Poly([0])
    	True
	>>> Poly([1, 2]) == Poly([1, 2, 0, 0])
	True
	>>> Poly([1, 1]) == Poly([1, 2])
        False
        """
        return cmp_poly(self.a, other.a)

    def __ne__(self, other):        # obsługa poly1 != poly2
        """ Funkcja zwracająca informację czy dwa wielomiany są od siebie różne 
        >>> Poly([1]) != Poly([1])
        False
        >>> Poly([1, 2]) != Poly([1, 2])
        False
        >>> Poly([0]) != Poly([0])
        False
        >>> Poly([0, 0, 0]) != Poly([0])
        False
        >>> Poly([1, 2]) != Poly([1, 2, 0, 0])
        False
        >>> Poly([1, 1]) != Poly([1, 2])
        True
	"""
        return not self == other

    def eval(self, x):        # schemat Hornera
        """ Funkcja zwracająca wynik przeprowadzonego schematu Hornera
            Evaluate polynomial.
        >>> Poly([3]).eval(1)
        3
        >>> Poly([3, 3]).eval(-1)
        0
        >>> Poly([4, 0, -1]).eval(2)
        0
        >>> Poly([1]).eval(2)
        1
        >>> Poly([0, 1]).eval(2)
        2
        >>> Poly([0, 0, 1]).eval(2)
        4
        >>> Poly([0, 0, 0, 1]).eval(2)
        8
        """
        return eval_poly(self.a, x)
    
    def combine(self, other):       # złożenie poly1(poly2(x))
        """ Funkcja zwracająca wynik złożenia wielomianów
        >>> Poly([1, 2, 3]).combine(Poly([1]))
        Poly([6])
        >>> Poly([1, 2, 3]).combine(Poly([1, 2]))
        Poly([6, 16, 12])
        >>> Poly([1, 2, 3]).combine(Poly([1, 2, 3]))
        Poly([6, 16, 36, 36, 27])
        """
        return Poly(combine_poly(self.a, other.a))
    
    def __pow__(self, n):      # poly(x)**n lub pow(poly(x),n)
        """ Funkcja zwracająca wielomian podniesiony do potęgi n
        >>> Poly([1]) ** 0
        Poly([1])
        >>> Poly([1, 2, 3]) ** 0
        Poly([1])
        >>> Poly([0]) ** 2
        Poly([0])
        >>> Poly([0]) ** 255
        Poly([0])
        >>> Poly([0]) ** 255
        Poly([0])
        >>> Poly([2]) ** 3
        Poly([8])
        >>> Poly([0, 2]) ** 3
        Poly([0, 0, 0, 8])
        >>> Poly([1, 2]) ** 2
        Poly([1, 4, 4])
        >>> Poly([1, 2]) ** 3
        Poly([1, 6, 12, 8])
        >>> Poly([1, 2, 3]) ** 2
        Poly([1, 4, 10, 12, 9])
        >>> Poly([1, 2, 3]) ** 3
        Poly([1, 6, 21, 44, 63, 54, 27])
        """
        return Poly(pow_poly(self.a, n))        
    
    def diff(self):            # różniczkowanie 
        """ Funkcja zwracająca wynik różniczkowania wielomianu
        >>> Poly([1]).diff()
        Poly([])
        >>> Poly([1, 2]).diff()
        Poly([2])
        >>> Poly([1, 2, 3]).diff()
        Poly([2, 6])
        >>> Poly([0, 0, 1]).diff()
        Poly([0, 2])
        >>> Poly([1, 0, 0]).diff()
        Poly([0, 0])
        """
        return Poly(diff_poly(self.a))
    
    def integrate(self):       # całkowanie
        """ Funkcja zwracająca wynik całkowania wielomianu 
        >>> Poly().integrate()
        Poly([0.0, 0.0])
        >>> Poly([1]).integrate()
        Poly([0.0, 1.0])
        >>> Poly([0, 2]).integrate()
        Poly([0.0, 0.0, 1.0])
        >>> Poly([1, 2]).integrate()
        Poly([0.0, 1.0, 1.0])
        >>> Poly([1, 2, 3]).integrate()
        Poly([0.0, 1.0, 1.0, 1.0])
        >>> Poly([0, 0, 0, 0, 5]).integrate()
        Poly([0.0, 0.0, 0.0, 0.0, 0.0, 1.0])
        """ 
        for i in range(len(self.a)):
            self.a[i] = self.a[i]/(i+1)
        self.a.insert(0,0.0)
        return self

    def is_zero(self):         # bool, True dla [0], [0, 0],...
        """ Funkcja zwracająca informację, czy wielomian jest zerem"""
        return is_zero(self.a)
    
if __name__ == '__main__':
    #test
    import doctest
    doctest.testmod()
