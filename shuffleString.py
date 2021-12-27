class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        char = ['']*len(s)
        for idx,i in enumerate(s):
            char[indices[idx]] = i
            
        return ''.join(char)