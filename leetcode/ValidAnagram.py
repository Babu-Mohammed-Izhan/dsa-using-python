# 438. Find All Anagrams in a String
# Medium

# 6544

# 241

# Add to List

# Share
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm = defaultdict(int)
        res = []
        if len(p) > len(s): 
            return []

        for ch in p: 
            hm[ch] += 1

        for i in range(len(p)-1):
            if s[i] in hm: hm[s[i]] -= 1
            
        for i in range(-1, len(s)-len(p)+1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i+len(p) < len(s) and s[i+len(p)] in hm: 
                hm[s[i+len(p)]] -= 1
                
            # check whether we encountered an anagram
            if all(v == 0 for v in hm.values()): 
                res.append(i+1)
                
        return res