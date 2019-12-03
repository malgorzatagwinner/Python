#!usr/bin/env python3
# -*- coding: utf -8-*-
import sys
import timeit

def P_rec(i, j):
    if i<= 0 and j<=0:
        return 0.5
    if j<=0:
        return 0.0
    if i<=0:
        return 0.0
    return 0.5 * (P_rec(i-1, j) + P_rec(i, j-1))

def P_dyn(i, j):
    TABLICA = [[0.5] + j*[0]]
    
    for x in range(1, i+1):
        TABLICA += [[1.0]]
        for y in range(1, j+1):
            TABLICA[x] += [0.5 * (TABLICA[x-1][y] + TABLICA[x][y-1])]

    return TABLICA[i][j]

if __name__ == '__main__':
    
    numer = 1000;
    
    print('P_rec: ', timeit.timeit('P_rec(7, 5)', setup='from __main__ import P_rec', number = numer))
    print('P_dyn: ', timeit.timeit('P_dyn(7, 5)', setup='from __main__ import P_dyn', number = numer))
