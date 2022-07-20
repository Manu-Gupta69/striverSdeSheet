# Problem Statement: Given a double x and integer n, calculate x raised to power n. Basically Implement pow(x, n).
# Examples:
# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Explanation: You need to calculate 2.00000 raised to 10 which gives ans 1024.00000
# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100
# Explanation: You need to calculate 2.10000 raised to 3 which gives ans 9.26100

# Time Complexity =  O(log n)
# Space Complexity: O(1)

def myPow(self, x: float, n: int) -> float:
    ans = 0
    nn = n
    if nn < 0:
        nn = -1 * nn
    while nn > 0:
        if nn%2 == 1:
            ans = ans * x
            nn -= 1
        else:
            x = x*x
            nn = nn/2
    if n < 0:
        ans = float(1.0/ans)
    return ans