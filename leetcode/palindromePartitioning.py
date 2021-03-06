
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]



class Solution:
    @cache
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, curr, res):
        if not s:
            res.append(curr)
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], curr+[s[:i]], res)
                
    def isPalindrome(self,s):
        return s == s[::-1]