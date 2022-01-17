# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

#! If length of digits is 0, return empty list
#! If length of digits is 1, return list with the numpad letters of the one of the numpad
#! Using recursion get previous and additional letters
#! for loop additional and prev add s+c and return array


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numpad = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(numpad[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = numpad[digits[-1]]
        return [s + c for s in prev for c in additional]