
# 347. Top K Frequent Elements
# Medium

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

#!  To find the k number of frequent elements.
#!  We have to create a list of 0s(bucket) and a dict.
#!  Loop through the array of numbers and add the number as key,
#!  Increment value by one if it appears in the array again.
#!  Once you have the dictionary of the frequencies of the numbers,
#!  Loop through the dictionary and replace the bucket value with the value of dictionary as index.
#!  Remove all the 0s in the bucket, reverse the list and return the first k values.

def topKFrequent(nums, k):
    #! Create a list of 0s
    bucket = [0 for _ in range(len(nums) + 1)]
    #! Create a dict that will store the frequencies
    num_counter = {}
    #! Loop through the array of numbers
    for i in nums:
        #! If the number is present in num_counter then increment value by 1 
        #! else intialize number with 1
        if i in num_counter.keys() :
            num_counter[i] = num_counter[i]+1
        else:
            num_counter[i] = 1
    #! Loop through num_counter and replace the bucket value with number
    #! Using frequency as index
    for num, freq in num_counter.items(): 
        bucket[freq] = num
    #! Remove all the zeros from the list
    flat_list = [item for item in bucket if item != 0]
    #! Return the reversed list of the first k values
    return flat_list[::-1][:k]

print(topKFrequent([1,1,1,2,2,3], 2))