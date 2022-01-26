# 1305. All Elements in Two Binary Search Trees
# Medium

# 1920

# 55

# Add to List

# Share
# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

 

# Example 1:


# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Example 2:


# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode, res=[]) -> List[int]:
        def inorder(node: TreeNode) -> None:
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        ans = []
        inorder(root1)
        inorder(root2)
        return sorted(ans)