#!/usr/bin/env python3
# -*- coding: utf -8-*-

def add_poly(poly1, poly2):
    length = min(len(poly1), len(poly2))
    out = [poly1[i] + poly2[i] for i in range(length)]
    
    out += poly1[length:]
    out += poly2[length:]
    return out


def sub_poly(poly1, poly2):         # poly1(x) - poly2(x)
    poly2 = [ -i for i in poly2]
    return add_poly(poly1, poly2)
    

def mul_poly(poly1, poly2):        # poly1(x) * poly2(x)
    out = [0]*(len(poly1) + len(poly2) -1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            out[i+j] += poly1[i] * poly2[j]
    
    while out[-1] == 0 and len(out) != 1:
        out.pop()
    
    return out
     
def is_zero(poly):      # bool, [0], [0,0], itp.
    for i in poly:
        if i != 0:
            return False
    return True

def cmp_poly(poly1, poly2):             # bool, porównywanie
    length = min(len(poly1), len(poly2))
    for i in range(length):
        if poly1[i] != poly2[i]:
            return False

    for j in range(length, len(poly2)):
        if poly2[j]!=0:
            return False
    
    for k in range(length, len(poly1)):
        if poly1[k]!=0:
            return False 
    return True

def eval_poly(poly, x0):           # poly(x0), algorytm Hornera
    out = 0
    for i in reversed(poly):
        out = i + x0 * out
    return out

def combine_poly(poly1, poly2):    # poly1(poly2(x)), trudne!
    out = [0]
    for i in reversed(poly1):
        out = add_poly([i], mul_poly(poly2, out))
    
    while out[-1] == '0' and len(out) != 1:
        out.pop()
    return out

def pow_poly(poly, n):             # poly(x) ** n
    out = [1] 
    t = poly 
    n = format(n, 'b') 
    for i in reversed(n): # lecimy od najmniej znaczaczych bitow
        if i == '1':
            out = mul_poly(t, out)
        t = mul_poly(poly,t)
    
    while out[len(out)-1] == '0':
        out.pop()

    return out

def diff_poly(poly):               # pochodna wielomianu
    for i in range(1, len(poly)):
        poly[i-1] = poly[i] * i
    return poly[:-1]

p1 = [2, 1]                   # W(x) = 2 + x
p2 = [-3, 0, 1]               # W(x) = -3 + x**2
p3 = [3]                      # W(x) = 3, wielomian zerowego stopnia
p4 = [0]                      # zero
p5 = [0, 0, 0]               # zero (niejednoznaczność)

import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x*x

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])
        self.assertEqual(add_poly([0], [0]), [0])
        self.assertEqual(add_poly([3], [0]), [3])
        self.assertEqual(add_poly([0], [3]), [3])
        
        
    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p2, self.p1), [0, -1, 1])
        self.assertEqual(sub_poly([0], [1,2]), [-1, -2])
        
    def test_mul_poly(self):
        self.assertEqual(mul_poly([0], [0]), [0])
        self.assertEqual(mul_poly([1], [0]), [0])
        self.assertEqual(mul_poly([0], [1]), [0])
        self.assertEqual(mul_poly([1], [1]), [1])
        self.assertEqual(mul_poly([0, 1], [1]), [0, 1])
        self.assertEqual(mul_poly([1], [0, 1]), [0, 1])
        self.assertEqual(mul_poly([0, 1], [0, 1]), [0, 0, 1])
        self.assertEqual(mul_poly([0, 2], [0, 2]), [0, 0, 4])
        self.assertEqual(mul_poly([0], [1, 2]), [0])

    def test_is_zero(self):
        self.assertEqual(is_zero([0]), True)
        self.assertEqual(is_zero([0,0,0]), True)
        self.assertEqual(is_zero([0,0,0,0,1]), False)


    def test_cmp_poly(self): 
        self.assertEqual(cmp_poly([0], [0]), True)
        self.assertEqual(cmp_poly([0],[0,0,0]), True)
        self.assertEqual(cmp_poly([0,0],[0,0,1]), False)

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p1,1),1)
        self.assertEqual(eval_poly(self.p1, 1), 1)
        self.assertEqual(eval_poly(self.p2, 2), 4)


    def test_combine_poly(self):
        self.assertEqual(combine_poly([1,2,3], [1,2]), [6,16,12])

    def test_pow_poly(self):
        self.assertEqual(pow_poly([1], 2), [1] )
        self.assertEqual(pow_poly([1], 5), [1] )
        self.assertEqual(pow_poly([0,1], 2), [0,0,1] )
        

    def test_diff_poly(self): 
        self.assertEqual(diff_poly([0,0,1]), [0,2])

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy


