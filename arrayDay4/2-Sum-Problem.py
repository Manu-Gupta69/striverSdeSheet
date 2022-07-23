# Problem Statement: Given an array of integers nums[] and an integer target, return indices of the two numbers such that their sum is equal to the target.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, 
# which is the required target, we return 
# indexes [0,1]. (0-based indexing)
# Example 2:
# Input Format: nums = [3,2,4,6], target = 6
# Output: [1,2]
# Explanation: Because nums[1] + nums[2] == 6, 
# which is the required target, we return 
# indexes [1,2].


def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashTable = {}
    for i in range(len(nums)):
        if target - nums[i] in  hashTable:
            return hashTable target-nums[i] , i
            
        else:
            hashTable[target-nums[i]] = i
    return -1