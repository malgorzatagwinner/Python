#!usr/bin/env python3
# -*- coding: utf -8-*-
import sys
import random as r
class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

# Wersja rekurencyjna wstawiania.
def bst_insert(top, node):   # zwraca nowy korzeń
    if top is None:
        return node
    if node.data < top.data:
        top.left = bst_insert(top.left, node)
    elif node.data > top.data:
        top.right = bst_insert(top.right, node)
    else:
        pass          # ignorujemy duplikaty
    return top            # bez zmian

def count_leafs(top):
    if top.left is None and top.right is None:
        return 1
    count = 0
    if top.left:
        count+=count_leafs(top.left)
    if top.right:
        count+=count_leafs(top.right)
    return count

def count_total(top):
    if top is None:
        return
    stack = list()
    stack.append(top)
    count = 0
    while stack:
        node = stack.pop()
        count+= node.data
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return count;

if __name__ == '__main__':

    root = Node(2)

    bst_insert(root, Node(2))
    bst_insert(root, Node(1))
    bst_insert(root, Node(5))
    bst_insert(root, Node(3))
    bst_insert(root, Node(6))
    assert(count_leafs(root) == 3)
    assert(count_total(root) == 17)
    bst_insert(root, Node(4))
    assert(count_leafs(root) == 3)
    assert(count_total(root) == 21)
    bst_insert(root, Node(0))
    bst_insert(root, Node(1.5))
    assert(count_leafs(root) == 4)
    assert(count_total(root) == 22.5)

