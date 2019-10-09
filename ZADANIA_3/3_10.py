#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys, random

roman_val = { 'I': 1, 'V' : 5, 'X' : 10, 'L': 50, 'C': 100, 'D' : 500, 'M' : 1000 }
def roman2int(line):
    line = line.strip()
    out = 0
    for i in range(len(line)):
        if(i+1!= len(line) and roman_val[line[i]] < roman_val[line[i+1]]):
            out -= roman_val[line[i]]
        else:
            out+= roman_val[line[i]]
    

    return out

if __name__ == '__main__':
    print(roman2int('MCMLXXXVII'))

    

