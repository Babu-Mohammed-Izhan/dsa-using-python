# A binary tree is uni-valued if every node in the tree has the same value.

# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

 

# Example 1:


# Input: root = [1,1,1,1,1,null,1]
# Output: true
# Example 2:


# Input: root = [2,2,2,5,2]
# Output: false



class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        vals = []
        
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        return len(set(vals)) == 1