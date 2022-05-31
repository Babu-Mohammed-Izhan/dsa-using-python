 #? 128. Longest Consecutive Sequence
#? Medium

#? Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

#? You must write an algorithm that runs in O(n) time.

 

#? Example 1:

#? Input: nums = [100,4,200,1,3,2]
#? Output: 4
#? Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#? Example 2:

#? Input: nums = [0,3,7,2,5,8,4,6,0,1]
#? Output: 9


#! To find the Longest Consecutive Sequence of numbers
def longestConsecutive(nums):
    #! If the length of the array is 0, then return 0
    if len(nums) == 0: 
        return 0
    #! Sort the array after converting it into a set to remove duplicate numbers
    nums = sorted(set(nums))
    #! Assign the first element of the array to last Number variable
    lastNum = nums[0]
    #! The current length of the consecutive array wiil be 1
    curLength = 1
    #! The result value is initialized to 1
    res = 1
    
    #! Loop through the array starting from the second element
    for i in range(1, len(nums)):
        #! If the current element is consecutive to the previous number, then increase curLength by 1
        if nums[i] == lastNum + 1:
            curLength += 1
        else:
        #! Else put current length to 1
            curLength = 1
        #! Assign res or curLength (Whichever is maximum) to res
        res = max(res, curLength)
        #! Put lastNum as the current element 
        lastNum = nums[i]
    #! Return result
    return res