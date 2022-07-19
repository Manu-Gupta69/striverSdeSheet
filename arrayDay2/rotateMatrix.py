# Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.
# Note: Rotate matrix 90 degrees anticlockwise
# Examples:
# Example 1:
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Explanation: Rotate the matrix simply by 90 degree clockwise and return the matrix.
# Example 2:
# Input: [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output:[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# Explanation: Rotate the matrix simply by 90 degree clockwise and return the matrix

# Time Complexity = O(N*N) + O(N*N).One O(N*N) for transposing the matrix and the other for reversing the matrix.
# Space Complexity: O(1)

def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()