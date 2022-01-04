import unittest


def validAnagram(s,t):
    #O(n^2)
    count=0
    if len(s) != len(t):
        return False
    for i in s:
        for j in t:
            if i == j:
                count += 1
    if count == len(s):
        return True
    else:
        return False

def validAnagramOn(s,t):

    # O(n) using Hashmap

    count=0
    characters = {}
    if len(s) != len(t):
        return False
    
    for i in s:
        characters[i] = i
    for i in t:
        if i in characters.keys():
            count += 1

    if count == len(s):
        return True
    else:
        return False        


class TestValidAnagram(unittest.TestCase):

    def test1(self):
        self.assertEqual(validAnagramOn('cat', 'tac'), True)
    
    def test2(self):
        self.assertEqual(validAnagramOn('program', 'function'), False)
    
    def test3(self):
        self.assertEqual(validAnagram('listen', 'silent'), True)

    def test4(self):
        self.assertEqual(validAnagram('asdfghj', 'aednfhs'), False)

if __name__ == '__main__':
    unittest.main()

# Run this file with a -v option to see all three test seperately
