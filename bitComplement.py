class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)
        complement = ""
        for i in binary[2:]:
            if i == '1':
                complement += '0'
            elif i == '0':
                complement += '1'
        result = int(complement, 2)
        return result