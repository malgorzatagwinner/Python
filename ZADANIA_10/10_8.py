#!usr/bin/env python3
# -*- coding: utf -8-*-
import sys
import random as r


class RandomQueue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def insert(self, item):
        self.items.append(item)            

    def remove(self):   # zwraca losowy element
        if len(self.items) == 0:
            raise RuntimeError("Lista jest pusta!")
        
        index = r.randint(0, len(self.items)-1)
        tmp = self.items[index]
        ostatni = self.items[-1]
        self.items[index] = ostatni
        x = self.items.pop()
        return tmp

    def is_empty(self):
        return len(self.items) == 0
    
    def is_full(self):
       return False 
    
    def clear(self):
       self.items = []

import unittest


class TestRandomQueue(unittest.TestCase):

    def test_insert(self):
        rq = RandomQueue()
        rq.insert(3)
        rq.insert(1)
        rq.insert(-48)
        rq.insert(42)
        self.assertEqual(str(rq), '[3, 1, -48, 42]')

    def test_remove(self):
        rq = RandomQueue()
        with self.assertRaises(Exception):
            rq.remove()

        items = [3, 1, -48, 42, (3, 2, 6), [12, -523], 'string']
        for item in items:
            rq.insert(item)

        while items:
            removed = rq.remove()
            print(rq) # żeby pokazać, że losowo
            self.assertIn(removed, items)
            items.remove(removed)

        self.assertEqual(items, [])

    def test_is_empty(self):
        rq = RandomQueue()
        self.assertTrue(rq.is_empty())
        rq.insert(3)
        rq.insert([3, 5])
        self.assertFalse(rq.is_empty())

    def test_clear(self):
        rq = RandomQueue()
        rq.insert(3)
        rq.insert(6)
        rq.clear()
        self.assertTrue(rq.is_empty())

if __name__ == "__main__":
    unittest.main()
