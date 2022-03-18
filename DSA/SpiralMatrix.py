'''
Spiral Matrix - Meduim

This question asks to return a list from a matrix in spiral form.

Here is an exmaple:
Input: matrix = [[1,2,3],
                [4,5,6],
                [7,8,9]]
Outputs: [1,2,3,6,9,8,7,4,5]

Notice that it starts from matrix[0][0] and continues to the right, then we traverse down, 
then left, then up, and right again until output is the equal to the amount of elements in the matrix

'''

def spiralMatrix(matrix):
    result = []
    if (matrix == None or len(matrix) == 0):
        return result
    
    top = 0 #top row
    bottom = len(matrix) - 1 #bottom row
    left = 0 #left column
    right = len(matrix[0]) - 1 # right row
    size = len(matrix) * len(matrix[0])

    while (len(result) < size):
        for i in range(left, right + 1): # left to right
            result.append(matrix[top][i])
        top += 1 # increment so that we don't double count the same number
        for i in range(top, bottom + 1):
            result.append(matrix[i][right]) # top to bottom
        right -= 1
        for i in range(right, left - 1, - 1): # go from left to right - stopping at left - 1 
            result.append(matrix[bottom][i])
        bottom -= 1
        for i in range(bottom, top - 1, - 1): # go from bottom to top
            result.append(matrix[i][left])
        left += 1
    return result

def main():
    print(spiralMatrix([[1,2,3], [4,5,6], [7,8,9]]))
    print(spiralMatrix([[1,2,3,4], [4,5,6,7], [8,9,10,11], [12,13,14,15]]))

if __name__ == "__main__":
    main()