"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        lengthRows = len(grid)
        lengthColumns = len(grid[0])
        count = 0

        def dfs(graph, row, column):
            if row in range(lengthRows) and column in range(lengthColumns) and graph[row][column] == '1':
                graph[row][column] = '0'
                dfs(graph, row + 1, column)
                dfs(graph, row - 1, column)
                dfs(graph, row, column + 1)
                dfs(graph, row, column - 1)
                return 1
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                currentPosition = grid[i][j]

                if currentPosition == '1':
                    count += dfs(grid, i, j)
        return count
