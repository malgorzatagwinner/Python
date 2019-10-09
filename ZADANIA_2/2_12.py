#!/usr/bin/env python3
# -*- coding: utf-8-*-
import sys

def firstchars(words):
    words = words.split()
    out = ''
    for char in words:
        first_char = char[0]
        out += first_char    
    print(out)

def lastchars(words):
    words = words.split()
    out = ''
    for char in words:
        last_char = char[len(char)-1]
        out += last_char
    print(out)

if __name__ == '__main__':
    #testy
    firstchars('kotek na ziemi')
    lastchars('piesek na drzewie')
