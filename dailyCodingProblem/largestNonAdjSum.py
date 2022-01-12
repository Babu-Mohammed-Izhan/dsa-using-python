# Good morning! Here's your coding interview problem for today.

# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev, cur = 0,0,0
        for i in nums:
            print(prev2, prev, cur)
            cur = max(prev, i + prev2)
            prev2 = prev
            prev = cur
        return cur