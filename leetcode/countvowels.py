# 1641. Count Sorted Vowel Strings
# Medium

# 1749

# 37

# Add to List

# Share
# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

# Example 1:

# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
# Example 2:

# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
# Example 3:

# Input: n = 33
# Output: 66045

class Solution:
    def countVowelStrings(self, n: int) -> int:
        seen = {}
        def dp(n,k):
            if k == 1 or n == 1:
                return k
            if (n,k) in seen:
                return seen[n,k]
            seen[n,k] = sum(dp(n-1,x) for x in range(1,k+1))
            return seen[n,k]
        return dp(n,5)