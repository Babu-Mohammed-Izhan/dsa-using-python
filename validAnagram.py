import unittest

# s='cat'
# t = 'tac'

def validAnagram(s,t):
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



class TestValidAnagram(unittest.TestCase):

    def test1(self):
        self.assertEqual(validAnagram('cat', 'tac'), True)
    
    def test2(self):
        self.assertEqual(validAnagram('program', 'function'), False)
    
    def test3(self):
        self.assertEqual(validAnagram('listen', 'silent'), True)

    def test4(self):
        self.assertEqual(validAnagram('asdfghj', 'aednfhs'), False)

if __name__ == '__main__':
    unittest.main()

# Run this file with a -v option to see all three test seperately
