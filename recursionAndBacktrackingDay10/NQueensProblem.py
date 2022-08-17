# Problem Statement: The n-queens is the problem of placing n queens on n × n chessboard such that no two queens can attack each other. Given an integer n, return all distinct solutions to the n -queens puzzle. Each solution contains a distinct boards configuration of the queen’s placement, where ‘Q’ and ‘.’ indicate queen and empty space respectively.

# Examples:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as 
# Let us first understand how can we place queens in a chessboard so that no attack on either of them can take place.

# Time Complexity: Exponential in nature since we are trying out all ways, to be precise it is O(N! * N).
# Space Complexity: O(N)

class Solution:
    def solve(self,row,col,posDia,negDia,result,n,board):
        if row == n:
            copy = [''.join(r) for r in board]
            result.append(copy)
            return
        for c in range(n):
            if not col[c] and not posDia[row+c] and not negDia[row-c]:
                board[row][c] = 'Q'
                col[c] = posDia[row+c] = negDia[row-c] = 1
                self.solve(row+1,col,posDia,negDia,result,n,board)
                col[c] = posDia[row+c] = negDia[row-c] = 0
                board[row][c] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        col = [0]*n
        posDia = [0]*(2*n-1)
        negDia = [0]*(2*n-1)
        result = []
        board = [['.']*n for i in range(n)]
        self.solve(0,col,posDia,negDia,result,n,board)
        return result