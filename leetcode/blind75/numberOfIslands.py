#? 200. Number of Islands
#? Medium

#? Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

#? An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

#? Example 1:

#? Input: grid = [
#?   ["1","1","1","1","0"],
#?   ["1","1","0","1","0"],
#?   ["1","1","0","0","0"],
#?   ["0","0","0","0","0"]
#? ]
#? Output: 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #! If not grid then return 0
        if not grid:
            return 0
        
        #! Initialize count to zero
        count = 0
        #! Traverse through the matrix using 2 for loops
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #! If the value in the grid is 1, then do dfs on the island
                if grid[i][j] == '1':
                    self.dfs(grid, i,j)
                    #! Then increase the count by 1
                    count += 1
        #! Return the count of the number of islands
        return count
    
    #! Dpeth first search will find the size of the island
    def dfs(self, grid, i , j):
        #! Check if i and j are out of bounds or not
        if i < 0 or j<0 or i>=len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        #! Replace all the 1s in the matrix to '#'
        grid[i][j] = "#"
        #! Traverse to top, bottom, right, left of current matrix
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)