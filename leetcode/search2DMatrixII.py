# 240. Search a 2D Matrix II
# Medium

# 7142

# 121

# Add to List

# Share
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
 

# Example 1:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
# Example 2:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false
 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix) - 1
        j = 0
        while True:
            
            if i < 0 or j >= len(matrix[0]):
                break
            
            if target < matrix[i][j]:
                i -= 1
            elif target > matrix[i][j]:
                j += 1
            else:
                return True
        return False