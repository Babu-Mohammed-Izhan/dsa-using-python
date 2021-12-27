class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        S=list(s)
        i=0
        j=len(s)-1
        while i < j:
            if not S[i].isalpha():
                i += 1
            elif not S[j].isalpha() :
                j -= 1
            else:
                S[i], S[j] = S[j], S[i]
                i , j = i+1, j-1
        return ''.join(S)