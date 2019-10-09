#!/usr/bin/env python3
# -*- coding: utf -8-*-
import sys

def sumaliter(line):
    line = line.split()
    out = 0
    for i in line:
        out+=len(i)
    print(out)

if __name__ == '__main__':
    sumaliter('Python jest super')
