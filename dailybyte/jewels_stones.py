import unittest

def jewels_stones(jewels, stones):
    jewel_map = {}
    stones_jewels = 0
    for i in jewels:
        jewel_map[i] = i
    for j in stones:
        if j in jewel_map.keys():
            stones_jewels += 1
    return stones_jewels

print(jewels_stones('abc', 'ac'))


class JewelsStones(unittest.TestCase):

    def test1(self):
        self.assertEqual(jewels_stones('abc', 'ac'), 2)
    
    def test2(self):
        self.assertEqual(jewels_stones('Af', 'AaaddfFf'), 3)
    
    def test3(self):
        self.assertEqual(jewels_stones('AYOPD', 'ayopd'), 0)

if __name__ == '__main__':
    unittest.main()
