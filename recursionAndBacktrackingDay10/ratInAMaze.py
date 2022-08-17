# Rat in a Maze
# Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N – 1, N – 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are ‘U'(up), ‘D'(down), ‘L’ (left), ‘R’ (right). Value 0 at a cell in the matrix represents that it is blocked and the rat cannot move to it while value 1 at a cell in the matrix represents that rat can travel through it.
# Note: In a path, no cell can be visited more than one time.
# Print the answer in lexicographical(sorted) order
# Examples:
# Example 1:
# Input:
# N = 4
# m[][] = {{1, 0, 0, 0},
#         {1, 1, 0, 1}, 
#         {1, 1, 0, 0},
#         {0, 1, 1, 1}}

# Output: DDRDRR DRDDRR

# Explanation:
# The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.
# Example 2:
# Input: N = 2
#        m[][] = {{1, 0},
#                 {1, 0}}
# Output:
#  No path exists and the destination cell is blocked.

# Time Complexity: O(4^(m*n)), because on every cell we need to try 4 different directions.
# Space Complexity:  O(m*n) ,Maximum Depth of the recursion tree(auxiliary space).

class Solution:
    def findPath(self, m, n):
        def solve(i,j,m,visited,s):
            if i == n-1 and j == n-1:
                if m[i][j] == 1:
                    result.append(s)
                    return
                else:
                    return
            if i < 0 or i >= n or j < 0 or j >= n or m[i][j] == 0 or visited[i][j] ==1:
                return
            visited[i][j] = 1
            solve(i+1,j,m,visited,s+'D')
            solve(i,j-1,m,visited,s+'L')
            solve(i,j+1,m,visited,s+'R')
            solve(i-1,j,m,visited,s+'U')
            visited[i][j] = 0

        result = []
        visited = [[0]*n for i in range(n)]
        if m[0][0] == 1:
            solve(0,0,m,visited,'')
        return result