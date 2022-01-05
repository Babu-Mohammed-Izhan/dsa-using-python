import unittest


def uncommonWords(string1, string2):
    # Time Complexity O(4n) = O(n)
    words1 = {}
    words2 = {}
    result = []
    arr1 = string1.split(" ")
    arr2 = string2.split(" ")
    for i in arr1:
        words1[i] = i
    for j in arr2:
        words2[j] = j
    for l in arr1:
        if l not in words2.keys():
            result.append(l)
    for k in arr2:
        if k not in words1.keys():
            result.append(k)
    return result

class TestUncommonWords(unittest.TestCase):

    def test1(self):
        self.assertEqual(uncommonWords("the quick","brown fox"), ["the", "quick", "brown", "fox"])
    
    def test2(self):
        self.assertEqual(uncommonWords("the tortoise beat the haire","the tortoise lost to the haire"), ["beat", "lost", "to"])
    
    def test3(self):
        self.assertEqual(uncommonWords("copper coffee pot","hot coffee pot"), ["copper", "hot"])

if __name__ == '__main__':
    unittest.main()

# Run this file with a -v option to see all three test seperately

