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
    rotten = set()
    fresh = set()

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            currentSpace = matrix[i][j]

            if currentSpace == 1:
                fresh.add(f"{i}{j}")
            elif currentSpace == 2:
                print("hello there")
    return "Hi there"
    


def main():
    print(rottingOranges("helo"))

if __name__ == "__main__":
    main()