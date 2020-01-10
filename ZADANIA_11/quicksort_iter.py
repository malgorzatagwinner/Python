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

def quicksort_iter(lista, begin, r):
    stos = [(begin, r)]
    while len(stos)!=0:
        a, b = stos.pop(-1)
        q = partition(lista, a, b)
            
        if q-1 > a:
            stos.append((a, q-1))
        if q+1 < b:
            stos.append((q+1, b))

if __name__ == '__main__':
    lista = [5, 1, 17, 224, 1, 2, 15, 221]
    for i in lista:
        print(i)

    quicksort_iter(lista, 0, len(lista)-1)
    print("Nowa lista")
    for i in lista:
        print(i)
