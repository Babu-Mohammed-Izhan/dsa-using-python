# Validate Stack Sequences
# Medium

# 3214

# 55

# Add to List

# Share
# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

 

# Example 1:

# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# Example 2:

# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # Initialize an array named stack 
        stack = []
        # Put i as 0
        i = 0
        # Iterate through the pushed list
        for x in pushed:
            # Append each number into an emoty array 
            stack.append(x)
            # Using a while loop, check if stack is empty or if the top of the stack is equal to current popped value
            while stack and stack[-1] == popped[i]:
                # Pop the stack once and increment it by one.
                stack.pop()
                i += 1
        # Check if stack is empty, if true sequnce is correct, then its not correct.
        return len(stack) == 0