# 680. Valid Palindrome II
# Easy

# 4607

# 267

# Add to List

# Share
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left]!= s[right]:
                delete_i = s[left:right]
                delete_j = s[left+1:right+1]
                return delete_i == delete_i[::-1] or delete_j == delete_j[::-1]
            left += 1
            right -= 1
        return True