# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
 
#! Solution
#! split s into an array of words
#! create both s and pattern into a set
#! If length is same then the pattern is matching
#! Also Check if original string and pattern have same length
#! And Check if the pattern order is the same with zip and set. 



class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        f = pattern
        t = s.split()
        return len(set(f)) == len(set(t)) == len(set(zip(f, t))) and len(f) == len(t)