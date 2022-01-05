# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


def serialize(root):
    s = ''
    if root == None:
        s += '-1'
    else:
        s += root.val

    if root != None:
        s += serialize(root.left)
        s += serialize(root.right)
    return s

def deserialize(s):

    return s

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = Node('root', Node('left', Node('left.left')), Node('right'))

# treeStructure
#          root
#        /      \
#    left     right
#     /
#   left.left
#
#


print(serialize(node))