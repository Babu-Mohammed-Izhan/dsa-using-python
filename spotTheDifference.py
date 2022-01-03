import unittest

def spotTheDifference (s , t):
    # O(n)
    characters = {}
    for i in s:
        characters[i] = i

    for i in t:
        if i not in characters.keys():
            return i

    return ""


class JewelsStones(unittest.TestCase):

    def test1(self):
        self.assertEqual(spotTheDifference('foobar', 'barfoot'), 't')
    
    def test2(self):
        self.assertEqual(spotTheDifference('ide', 'idea'), 'a')
    
    def test3(self):
        self.assertEqual(spotTheDifference('coding', 'ingcod'), '')

if __name__ == '__main__':
    unittest.main()