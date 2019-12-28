#!usr/bin/env python3
# -*- coding: utf -8-*-

def partition(lista, begin, r):
    x = lista[r]
    a = begin - 1
    for i in range(begin, r):
        if(lista[i] <= x):
            a = a+1
            lista[a], lista[i] = lista[i], lista[a]
    lista[a+1], lista[r] = lista[r], lista[a+1]
    return a+1

def sorted(lista, begin, r):
    for i in range(begin, r):
        if(lista[i] > lista[i+1]):
            return False
    return True

def quicksort_iter(lista, begin, r):
    stos = [(begin, r)]
    while len(stos)!=0:
        a, b = stos[-1]
        stos.pop(-1)
        if( not sorted(lista, a, b)):
            q = partition(lista, a, b)
            stos.append((a, q-1))
            stos.append((q+1, b))

if __name__ == '__main__':
    lista = [5, 1, 17, 224, 1, 2, 15, 221]
    for i in lista:
        print(i)

    quicksort_iter(lista, 0, len(lista)-1)
    print("Nowa lista")
    for i in lista:
        print(i)
