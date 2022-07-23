# Problem Statement: Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to B.
# Examples:
# Input Format:  A = [4, 2, 2, 6, 4] , B = 6
# Result: 4
# Explanation: The subarrays having XOR of their elements as 6 are  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]
# Input Format: A = [5, 6, 7, 8, 9], B = 5
# Result: 2
# Explanation:The subarrays having XOR of their elements as 2 are [5] and [5, 6, 7, 8, 9]

# Time Complexity: O(N)
# Space Complexity: O(N)

def solve(self, A, B):
    hashSet = {}
    Xor = 0
    count = 0
    for i in range(A):
        Xor = Xor^A[i]
        if Xor == B:
            count += 1
        if Xor^B in hashSet:
            count+= hashSet[Xor^B]
        hashSet[Xor^B] += 1
    return count
