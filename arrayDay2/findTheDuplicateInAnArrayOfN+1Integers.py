# Problem Statement: Given an array of N + 1 size, where each element is between 1 and N. Assuming there is only one duplicate number, your task is to find the duplicate number.
# Examples:
# Example 1: 
# Input: arr=[1,3,4,2,2]
# Output: 2
# Explanation: Since 2 is the duplicate number the answer will be 2.
# Example 2:
# Input: [3,1,3,4,2]
# Output:3
# Explanation: Since 3 is the duplicate number the answer will be 3.

# Time complexity: O(N). Since we traversed through the array only once.
# Space complexity: O(1).

def findDuplicate(self, nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if fast == slow:
            break
    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
    