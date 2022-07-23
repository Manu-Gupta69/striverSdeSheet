# Problem Statement: Given a matrix m X n, count paths from left-top to the right bottom of a matrix with the constraints that from each cell you can either only move to the rightward direction or the downward direction.
# Example 1:
# Input Format: m = 2, n= 2
# Output: 2
# Explanation: From the top left corner there are total 2 ways to reach the bottom right corner:

# Time Complexity: The time comp[lexity of this recursive solution is exponential.
# Space Complexity: As we are using stack space for recursion so the space complexity will also be exponential.
def uniquePaths(self, m: int, n: int) -> int:
    visited_path = {}
    
    def recur(i, j, visited_path):
        if i == m-1 or j == n-1:
            return 1

        if (i, j) in visited_path:
            return visited_path[(i, j)]
        
        visited_path[(i,j)] = recur(i, j+1, visited_path) + recur(i+1, j, visited_path)
        return visited_path[(i,j)]
    
    return recur(0,0, visited_path)