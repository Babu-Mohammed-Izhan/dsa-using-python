# 923. 3Sum With Multiplicity
# Medium

# 1907

# 226

# Add to List

# Share
# Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

# As the answer can be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation: 
# Enumerating by the values (arr[i], arr[j], arr[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
# Example 2:

# Input: arr = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation: 
# arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        c = collections.Counter(arr)
        res = 0
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k: 
                res += c[i] * (c[i] - 1) * (c[i] - 2) / 6
            elif i == j != k: 
                res += c[i] * (c[i] - 1) / 2 * c[k]
            elif k > i and k > j: 
                res += c[i] * c[j] * c[k]
        return int(res % (10**9 + 7))