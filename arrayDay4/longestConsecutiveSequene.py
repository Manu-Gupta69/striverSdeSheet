# Problem Statement: You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.
# Examples:
# Example 1:
# Input: [100, 200, 1, 3, 2, 4]
# Output: 4
# Explanation: The longest consecutive subsequence is 1, 2, 3, and 4.
# Input: [3, 8, 5, 7, 6]
# Output: 4
# Explanation: The longest consecutive subsequence is 5, 6, 7, and 8.

# Time Complexity: The time complexity of the above approach is O(N) because we traverse each consecutive subsequence only once.
# Space Complexity: The space complexity of the above approach is O(N) because we are maintaining a HashSet.

def longestConsecutive(self, nums: List[int]) -> int:
    hashSet = set(nums)
    longestStreak = 0
    currentStreak = 0
    for i in nums:
        if i-1 not in hashSet:
            currentNum = i
            currentStreak = 1
            while currentNum+1 in hashSet:
                currentStreak += 1
                currentNum += 1
        longestStreak = max(longestStreak,currentStreak)
    return longestStreak

