 #? Given the root of a binary tree, return its maximum depth.

#? A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


#? Example 1:

#? Input: root = [3,9,20,null,null,15,7]
#? Output: 3

#! To find the maximum depth of a binary tree,
#! We have to use Depth First Search to find the longest path
#! Use recursion of dfs function to traverse the tree
#! return the maximum of left or right branch of the subtrees
#! of the current node


def maxDepth(self, root: Optional[TreeNode]) -> int:
    def dfs(root, depth):
        if not root: 
            return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                    
    return dfs(root, 0)

