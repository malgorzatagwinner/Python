#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def miarka(number):
    """ Zwraca miarke o podanym rozmiarze     
    >>> miarka(3)
    '|....|....|....|\\n0    1    2    3'
    >>> miarka(0)
    '|\\n0'
    >>> miarka(12)
    '|....|....|....|....|....|....|....|....|....|....|....|....|\\n0    1    2    3    4    5    6    7    8    9   10   11   12'
    """
    out = "|" + "....|" * number + "\n" + "0"
    for i in range(number):
        out+= str(i+1).rjust(5)
    return(out)
        
def wymiary(prompt):
    while(True):
        line = input(prompt)
        try:
            number = int(line)
        except ValueError:
            print("Ta wartosc nie jest liczba! Sprobuj jeszcze raz!")
        else:
            return number

def prostokat():
    szerokosc = wymiary("Podaj szerokosc prostokata: ")
    wysokosc = wymiary("Podaj wysokosc prostokata: ")
    srodek = ("|" + "   |"  * szerokosc + "\n")
    brzeg = ("+" + "---+"*szerokosc +"\n")
    out = (brzeg + srodek)*wysokosc + brzeg
    return out

if __name__ == '__main__':
    # testy
    # na standardowym wejściu
    data = int(input("Podaj dlugosc miarki: "))
    print(miarka(data))
    print(prostokat())
