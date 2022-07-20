# Problem Statement: Given an m*n 2D matrix and an integer, write a program to find if the given integer exists in the matrix.
# Given matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row
# Example 1:
# Input: matrix = 
# [[1,3,5,7],
#  [10,11,16,20],
#  [23,30,34,60]], 
# target = 3
# Output: true
# Explanation: As the given integer(target) exists in the given 2D matrix, the function has returned true.
# Example 2:
# Input: matrix = 
# [[1,3,5,7],
#  [10,11,16,20],
#  [23,30,34,60]], 
# target = 13
# Output: false
# Explanation: As the given integer(target) does not exist in the given 2D matrix, the function has returned false.

# Time Complexity = O(log(m*n))
# Space Complexity = O(1)

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    if not n:
        return False
    start = 0
    end = n*m-1
    while start < end:
        mid = int(start + (end-start)/2)
        if matrix[mid//m][mid%m] == target:
            return True
        elif matrix[mid//m][matrix%m] < target:
            start = mid+1
        else:
            end = mid-1
    return False
    
        