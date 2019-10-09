#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def najdluzszy(line):
    line = line.split()
    out = ''
    out_len = 0;
    for i in line:
        if out_len < len(i):
            out_len = len(i)
            out = i

    print("Najdluzsze slowo: ", out, ", jego dlugosc: ", out_len)

if __name__ == '__main__':
    #testy
    najdluzszy('mama tata dziadek pradziadek prapradziadek')
