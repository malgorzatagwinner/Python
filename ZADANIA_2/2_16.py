#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def zmiana(line):
    line = line.replace('GvR', 'Guido van Rossum')
    print(line)

if __name__ == '__main__':
    #testy
    zmiana('GvR byl najlepszym malarzem z linii wszystkich GvR')

