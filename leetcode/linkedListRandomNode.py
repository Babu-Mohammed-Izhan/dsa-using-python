# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

# Implement the Solution class:

# Solution(ListNode head) Initializes the object with the integer array nums.
# int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be choosen.
 

# Example 1:


# Input
# ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
# [[[1, 2, 3]], [], [], [], [], []]
# Output
# [null, 1, 3, 2, 2, 3]

# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.getRandom(); // return 1
# solution.getRandom(); // return 3
# solution.getRandom(); // return 2
# solution.getRandom(); // return 2
# solution.getRandom(); // return 3
# getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
 

# Constraints:

# The number of nodes in the linked list will be in the range [1, 104].
# -104 <= Node.val <= 104
# At most 104 calls will be made to getRandom.


#! It uses Reservoir Sampling
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        

    def getRandom(self) -> int:
        reservoir = self.head.val
        i = 2
        next = self.head.next
        while next :
            if random.random() < 1/i:
                reservoir = next.val
            
            i +=1
            next = next.next
    
        return reservoir
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)