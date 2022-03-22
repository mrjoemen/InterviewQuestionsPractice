'''

We are given an m x n grid where each cell can have one of three values:

0 is an empty cell,
1 is a fresh orange, or
2 is a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent (up, down, left, right) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

example:
input = [[2,1,1],   [[2,2,1],   [[2,2,2],   [[2,2,2],   [[2,2,2],
         [1,1,0], -> [2,1,0], -> [2,2,0], -> [2,2,0], -> [2,2,0],
         [0,1,1]]    [0,1,1]]    [0,1,1]]    [0,2,1]]    [0,2,2]]

        minute 0                                        minute 4
output = 4 

'''

def rottingOranges(matrix):
    rotten = set() #these sets will contain the coordinates of all rotten oranges
    fresh = set() #these sets will contain the coordinates of all fresh oranges

    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[row])):
            currentSpace = matrix[row][column]

            if currentSpace == 1:
                fresh.add(f"{row}{column}") # coors
            elif currentSpace == 2:
                rotten.add(f"{row}{column}")
    minutes = 0
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]] #down, right, left, up

    while len(fresh) > 0: #while there are fresh oranges, check if we can infect
        infected = set()

        for coordinates in rotten:
            x = int(coordinates[0]) #x-axis row
            y = int(coordinates[1]) #y-axis column
            for direction in directions:
                nextX = x + direction[0]
                nextY = y + direction[1]

                if f"{nextX}{nextY}" in fresh:
                    fresh.remove(f"{nextX}{nextY}")
                    infected.add(f"{nextX}{nextY}")
        if len(infected) == 0:
            return -1

        rotten = infected
        minutes += 1
    return minutes
    


def main():
    print(rottingOranges([[2,1,1], [1,1,0], [0,1,1]]))



if __name__ == "__main__":
    main()