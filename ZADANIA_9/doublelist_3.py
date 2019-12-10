#!usr/bin/env python3
# -*- coding: utf -8-*-
import sys

N = 100000
class Node:
    """Klasa reprezentująca węzeł listy dwukierunkowej."""

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DoubleList:
    """Klasa reprezentująca całą listę dwukierunkową."""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node     # stary head
            self.head = node          # nowy head
        else:         # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.tail:
            node.prev = self.tail
            self.tail.next = node     # stary tail
            self.tail = node          # nowy tail
        else:         # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def remove_head(self):   # zwraca node
        if self.head is None:
            raise ValueError("pusta lista")
        elif self.head is self.tail:
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.head
            self.head = self.head.next
            self.head.prev = None   # czyszczenie
            self.length -= 1
            return node

    def remove_tail(self):   # zwraca node
        if self.head is None:
            raise ValueError("pusta lista")
        elif self.head is self.tail:
            node = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None   # czyszczenie
            self.length -= 1
            return node

    def find_max(self):
    # Zwraca łącze do węzła z największym kluczem.
        if(self.length == 0):
            raise ValueError("Pusta lista")
        tmp = self.head
        node = self.head
        while(node).next:
            if(node.next.data > tmp.data):
                tmp = node.next
            node = node.next
        return tmp

    def find_min(self):
    # Zwraca łącze do węzła z najmniejszym kluczem.
        if(self.length == 0):
            raise ValueError("Pusta lista")
        tmp = self.head
        node = self.head
        while(node.next):
            if(node.next.data < tmp.data):
                tmp = node.next
            node = node.next
        return tmp

    def remove(self, node):
    # Usuwa wskazany węzeł z listy.
        if self.head is None:
            raise ValueError("pusta lista")
        poprzedni = node.prev
        nastepny = node.next
        poprzedni.next = nastepny
        nastepny.prev = poprzedni
        node.data = None
        node.prev = None
        node.nect = None
        self.length -=1

    def clear(self):     # czyszczenie list
        node = self.head
        while(node):
            node.prev = None
            node.data = None
            node = node.next

    def output(self):
        node = self.head

        while node is not None:
            print(node.data)
            node = node.next


if __name__ == '__main__':
    lista = DoubleList()
    pierwszy = Node(2)
    drugi = Node(8)
    trzeci = Node (7)
    czwarty = Node(13)
    piaty = Node(1)
    szosty = Node(4)
    lista.insert_head(pierwszy)
    lista.insert_tail(drugi)
    lista.insert_tail(trzeci)
    lista.insert_tail(czwarty)
    lista.insert_tail(piaty)
    lista.insert_tail(szosty)
    assert(lista.find_min() == piaty)
    assert(lista.find_max() == czwarty)
    lista.remove(drugi)
    assert(lista.count() == 5)
    lista.output()
