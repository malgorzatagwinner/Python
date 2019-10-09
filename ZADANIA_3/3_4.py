#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

while True:
    line = input("Podaj liczbe: ")
    if line == 'stop':
        break
    try:
        number = int(line)
    except ValueError:
        print('Blad, prosze wpisac liczbe rzeczywista typu float')
    else:
        print(number, pow(number, 3))
