# LeetCode Problem Medium 1010

# You are given a list of songs where the ith song has a duration of time[i] seconds.

# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.




class Solution:

    #O(n^2)

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs = 0
        for i in range(len(time)):
            for j in range(i,len(time)):
                if i != j:
                    if (time[i] + time[j]) % 60 == 0:
                        pairs += 1
        
        return pairs