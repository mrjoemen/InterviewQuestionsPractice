"""
You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.

https://leetcode.com/problems/where-will-the-ball-fall/

--

the trick here is to use a dfs

"""



def whereWillTheBallFall(grid: List[List[int]]) -> List[int]:
    lengthOfRows = len(grid)
    lengthOfColumns = len(grid[0])

    def candrop(i, j):
        # i = row j = column
        if i == lengthOfRows: # if we get to the bottom of the list
            return j
        if j == lengthOfColumns - 1 and grid[i][j] == 1: # if we are the right of the grid, and it redirects to the right
            return -1
        if j == 0 and grid[i][j] == -1: # if we are the left of the grid, and the it redirects to the left
            return -1
        if grid[i][j] == 1 and grid[i][j+1] == -1: # if currentPosition redirects right and the next grid redirects left
            return -1
        if grid[i][j] == -1 and grid[i][j-1] == 1: # if currentPosition redirects left and the grid before redirects right
            return -1
        return candrop(i + 1, j + grid[i][j]) # increment row and go next column
    
    return [candrop(0, j) for j in range(lengthOfColumns)]