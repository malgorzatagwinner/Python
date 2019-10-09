#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def miarka():
    while(True):
        line = input("Podaj długosc miarki: ")
        try:
            number = int(line)
        except ValueError:
            print("Ta wartosc nie jest liczba! Sprobuj jeszcze raz!")
        else:
            out = "|" + "....|" * number + "\n" + "0"
            for i in range(number):
                out+= str(i+1).rjust(5)
            print(out)
            break


miarka()
