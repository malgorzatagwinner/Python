#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def wymiary(prompt):
    while(True):
        line = input(prompt)
        try:
            number = int(line)
        except ValueError:
            print("Ta wartosc nie jest liczba! Sprobuj jeszcze raz!")
        else:
            return number

szerokosc = wymiary("Podaj szerokosc prostokata: ")
wysokosc = wymiary("Podaj wysokosc prostokata: ")
srodek = ("|" + "   |"  * szerokosc + "\n")
brzeg = ("+" + "---+"*szerokosc +"\n")
out = (brzeg + srodek)*wysokosc + brzeg
print(out)
