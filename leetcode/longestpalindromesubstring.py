# 5. Longest Palindromic Substring
# Medium

# 16737

# 982

# Add to List

# Share
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i),self.helper(s,i,i+1),res, key=len)
        return res
    def helper(self, s, l , r):
        while 0 <= l and r < len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]