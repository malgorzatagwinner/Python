#!usr/bin/env python3
# -*- coding: utf -8-*-
import sys

class Stack:
    def __init__(self, size):
        self.items = [None]* size
        self.size = size
        self.pomocnicza = [False] * size
        self.last_index = 0

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.last_index == 0

    def is_full(self):
        return self.last_index == self.size-1

    def push(self, item):
        if(item < self.size and item >= 0):
            if not self.pomocnicza[item]:
                self.items[self.last_index] = item
                self.last_index = self.last_index + 1
                self.pomocnicza[item] = True

    def pop(self):
        if self.last_index == 0:
            raise RuntimeError("Pusty stos!")
        self.last_index -=1
        tmp = self.items[self.last_index]
        self.items[self.last_index] = None
        return tmp

    def clear(self):
        self.items = [None]* self.size
        self.pomocnicza = [False] * self.size
        self.last_index = 0

import unittest


class TestStack(unittest.TestCase):

    def test_push(self):
        rq = Stack(4)
        rq.push(0)
        rq.push(1)
        rq.push(3)
        rq.push(42)
        rq.push(2)
        self.assertEqual(str(rq), '[0, 1, 3, 2]')

    def test_pop(self):
        rq = Stack(4)
        with self.assertRaises(Exception):
            rq.pop()

        items = [3, 1, 2, 0]
        for item in items:
            rq.push(item)

        while items:
            popped = rq.pop()
            self.assertIn(popped, items)
            items.remove(popped)

        self.assertEqual(items, [])

    def test_is_empty(self):
        rq = Stack(666666)
        self.assertTrue(rq.is_empty())
        rq.push(3)
        rq.push(5)
        self.assertFalse(rq.is_empty())

    def test_clear(self):
        rq = Stack(10)
        rq.push(3)
        rq.push(6)
        rq.clear()
        self.assertTrue(rq.is_empty())

if __name__ == "__main__":
    unittest.main()
