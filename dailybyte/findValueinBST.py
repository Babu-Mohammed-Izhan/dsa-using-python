# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:


# Input: root = [4,2,7,1,3], val = 5
# Output: []

#         3
#        / \
#       1   4
# and the search value 1 return a reference to the node containing 1.
# Ex: Given the following tree...

#         7
#        / \
#       5   9
#          / \ 
#         8   10
# and the search value 9 return a reference to the node containing 9.
# Ex: Given the following tree...

#         8
#        / \
#       6   9
# and the search value 7 return null.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and val < root.val:
            return self.searchBST(root.left, val)
        if root and val > root.val:
            return self.searchBST(root.right, val);
        return root