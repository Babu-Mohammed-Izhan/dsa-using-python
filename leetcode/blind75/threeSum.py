# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]


#!  [-1,0,1,2,-1,-4]
#!    | |         |
#!    i l         r
#!  loop through the array with i 
#!  Create left and right pointers at start and end of the array
#!  Add l,i,r
#!  If res < 0 then increment l
#!  If res > 0 then decrement r
#!  if res = 0 then add all three values to final result array
#!  Now move both l and r inside
#!  Do this for all numbers
#?  Range 0 to len(nums)-2




def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        #! Checks if i is greater than 0 and if the current number is the same as the previous one.
        if i>0 and nums[i] == nums[i-1]:
            continue
        #! Assign pointer left and right ( left = next value, right = last value of the array )
        l, r = i+1, len(nums)-1
        while l<r:
            #! Add the current number, left and right pointer number
            s = nums[i] + nums[l] + nums[r]
            #! if result is less than 0 then move left pointer to the right
            if s < 0:
                l += 1
            #! if result is greater than 0 then move right pointer to the left
            elif s > 0:
                r -= 1;
            #! if result is 0 then append the array of numbers to the array and move both pointers to the inside
            else:
                res.append((nums[i], nums[l], nums[r]))
                #! If the value on the right of the left pointer is the same then move the pointer again to the right
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                #! If the value on the left of the right pointer is the same then move the pointer again to the left
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return res


print(threeSum([-1,0,1,2,-1,-4]))