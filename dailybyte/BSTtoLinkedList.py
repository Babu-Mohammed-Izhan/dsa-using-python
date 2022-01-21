# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

# Example 1:


# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [0]
# Output: [0]



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#! The prospect of solving this problem in O(1) might look tricky in the beginning, but all you need to know is how preorder traversal works.
#! The key intuition of this solution is to preserve the "Pre-Order" order as we go.

#! So we maintain a pointer curr while going down the tree. If curr has a left child, we want to shift it to the right while preserving the order. This will be two step process.
#! Create another pointer p to find the right most point in the left subtree. Then we shift the contents of curr.right into p.right. The tree which we have right now (stage 2 in image) if you notice, still gives the exact same preorder traversal. So now we just shift this to the right of curr.

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                runner = curr.left
                while runner.right: 
                    runner = runner.right
                runner.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
