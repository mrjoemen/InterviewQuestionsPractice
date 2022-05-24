"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

link: https://leetcode.com/problems/max-area-of-island/

solution: https://www.youtube.com/watch?v=W8VuDt0eb5c


"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # this question is pretty similar to num of islands
        answer = 0
        n = len(grid)
        m = len(grid[0])

        def dfs(val1, val2):
            count = 0 # this is practically the main difference, we are keeping track of how many 1 are in a given island
            if val1 in range(n) and val2 in range(m) and grid[val1][val2] == 1:
                grid[val1][val2] = 0
                count += 1
                count += dfs(val1 - 1, val2)
                count += dfs(val1 + 1, val2)
                count += dfs(val1, val2 - 1)
                count += dfs(val1, val2 + 1)
                return count
            else:
                return count

        for i in range(n):
            for j in range(m):
                answer = max(answer, dfs(i, j))
        return answer