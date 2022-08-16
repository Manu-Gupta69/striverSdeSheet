# Problem Statement: Given N and K, where N is the sequence of numbers from 1 to N([1,2,3….. N]) find the Kth permutation sequence.
# For N = 3  the 3!  Permutation sequences in order would look like this:-
# Note: 1<=K<=N! Hence for a given input its Kth permutation always exists
# Examples:

# Example 1:
# Input: N = 3, K = 3
# Output: “213”
# Explanation: The sequence has 3! permutations as illustrated in the figure above. K = 3 corresponds to the third sequence.

# Example 2:
# Input: N = 3, K = 5 
# Result: “312”
# Explanation: The sequence has 3! permutations as illustrated in the figure above. K = 5 corresponds to the fifth sequence.


# Time Complexity: O(N) * O(N) = O(N^2)
# Reason: We are placing N numbers in N positions. This will take O(N) time. For every number, we are reducing the search space by removing the element already placed in the previous step. This takes another O(N) time.

# Space Complexity: O(N) 
# Reason: We are storing  the numbers in a data structure(here vector)


def getPermutation(self, n: int, k: int) -> str:
    num = []
    fact = 1
    for i in range(1,n):
        fact *= i
        num.append(i)
    num.append(n)
    ans = ""
    k = k-1
    while True:
        ans += str(num.pop(int(k/fact)))
        if len(num) == 0:
            break
        k = k % fact
        fact = fact/len(num)
    return ans