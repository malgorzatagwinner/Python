#!usr/bin/env python3
# -*- coding: utf -8-*-

def cmp(a, b):
    return (a > b) - (a < b)

class PriorityQueue:
    def __init__(self, cmpfunc = cmp):
        self.items = []
        self.cmpfunc = cmpfunc

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return False

    def insert(self, data):
        self.items.append(data)

    def remove(self):
        if len(self.items) == 0:
            raise RuntimeError('Pusta lista!')
        # Etap 1 - wyszukiwanie elementu.
        maxi = 0
        for i in range(len(self.items)):
            if self.cmpfunc(self.items[i], self.items[maxi]) > 0:
                maxi = i
        # Etap 2 - usuwanie elementu.
        data = self.items[maxi]
        self.items[maxi] = self.items[-1]
        self.items.pop()   # usuwamy referencję
        return data

import unittest


class TestStack(unittest.TestCase):

    def test_insert(self):
        rq = PriorityQueue()
        rq.insert(0)
        rq.insert(1)
        rq.insert(3)
        rq.insert(42)
        rq.insert(2)
        self.assertEqual(str(rq.items), '[0, 1, 3, 42, 2]')

    def test_remove(self):
        rq = PriorityQueue()
        with self.assertRaises(RuntimeError):
            rq.remove()

        items = [3, 1, 2, 0, -48, 42]
        for item in items:
            rq.insert(item)

        items = list(sorted(items))
        while items:
            popped = rq.remove()
            self.assertEqual(popped, items.pop())

        self.assertEqual(items, [])

    def test_custom_function(self):
        rq = PriorityQueue(lambda x, y: x[1] > y[1])
        with self.assertRaises(RuntimeError):
            rq.remove()

        items = [
            ('a', 3),
            ('beautiful', 2),
            ('is', 4),
            ('place', 1),
            ('world', 5)
        ]
        for item in items:
            rq.insert(item)

        while items:
            popped = rq.remove()
            self.assertIn(popped, items)
            items.remove(popped)

        self.assertEqual(items, [])

    def test_is_empty(self):
        rq = PriorityQueue()
        self.assertTrue(rq.is_empty())
        rq.insert(3)
        rq.insert(5)
        self.assertFalse(rq.is_empty())

if __name__ == "__main__":
    unittest.main()
