# Problem Statement:

# Given a 9×9 incomplete sudoku, solve it such that it becomes valid sudoku. Valid sudoku has the following properties.
#          1. All the rows should be filled with numbers(1 – 9) exactly once.
#          2. All the columns should be filled with numbers(1 – 9) exactly once.
#          3. Each 3×3 submatrix should be filled with numbers(1 – 9) exactly once.
# Note: Character ‘.’ indicates empty cell.

# Explanation:
#  The empty cells are filled with the possible numbers. There can exist many such arrangements of numbers. The above solution is one of them. Let’s see how we can fill the cells below.

# Time Complexity: O(9(n ^ 2)), in the worst case, for each cell in the n2 board, we have 9 possible numbers.
# Space Complexity: O(1), since we are refilling the given board itself, there is no extra space required, so constant space complexity.

class Solution:
    def solve(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
     
                    for c in range(1,10):
                        if self.isValid(board,i,j,c):
                            board[i][j] = str(c)
                        
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'

                    return  False
        return True
    
    def isValid(self,board,row,col,c):
        for i in range(len(board)):
            if board[row][i] == str(c):
                return False
            if board[i][col] == str(c):
                return False
            if board[3*(row//3)+(i//3)][3*(col//3)+i%3] == str(c):
                return False
        return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)