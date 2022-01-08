import unittest


# Good morning! Here's your coding interview problem for today.

# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.

def create_arr(a,b):
    return [a,b]

def car(pair):
    arr = pair(create_arr)
    return arr[0]

def cdr(pair):
    arr = pair(create_arr)
    return arr[1]


class TestlistSumFind(unittest.TestCase):

    def test1(self):
        self.assertEqual(car(cons(3,4)), 3)
    
    def test2(self):
        self.assertEqual(cdr(cons(3,4)), 4)
    
    def test3(self):
        self.assertEqual(cdr(cons(3,10)), 10)

if __name__ == '__main__':
    unittest.main()

# Run this file with a -v option to see all three test seperately