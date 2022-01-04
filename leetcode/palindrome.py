class Solution:
    def isPalindrome(self, s: str) -> bool:
        final = ''.join(ch for ch in s if ch.isalnum()).lower()
        return final == final[::-1]
            