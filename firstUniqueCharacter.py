import unittest

def firstUniqChar (string):
    #O(n)
    characters = {}
    for i in string:
        if i not in characters.keys():
            characters[i] = 0
        else:
            characters[i] += 1
    for j in characters.items():
        if j[1] == 0 :
            return string.find(j[0])
    return -1



class TestTwoSum(unittest.TestCase):

    def test1(self):
        self.assertEqual(firstUniqChar("abcabd"), 2)
    
    def test2(self):
        self.assertEqual(firstUniqChar("thedailybyte"), 1)
    
    def test3(self):
        self.assertEqual(firstUniqChar("aaaaaabbbbb"), -1)

if __name__ == '__main__':
    unittest.main()

# Run this file with a -v option to see all three test seperately
