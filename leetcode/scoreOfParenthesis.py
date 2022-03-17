# 856. Score of Parentheses
# Medium

# 3919

# 120

# Add to List

# Share
# Given a balanced parentheses string s, return the score of the string.

# The score of a balanced parentheses string is based on the following rule:

# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
 

# Example 1:

# Input: s = "()"
# Output: 1
# Example 2:

# Input: s = "(())"
# Output: 2
# Example 3:

# Input: s = "()()"
# Output: 2


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        curr = 0
        for i in s:
            if i == '(':
                stack.append(curr)
                curr = 0
            else:
                curr+= stack.pop() + max(curr,1)
        return curr