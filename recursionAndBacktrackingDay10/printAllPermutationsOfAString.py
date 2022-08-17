# Problem Statement: Given an array arr of distinct integers, print all permutations of String/Array.
# Examples:
# Example 1: 
# Input: arr = [1, 2, 3]
# Output: 
# [
#   [1, 2, 3],
#   [1, 3, 2],
#   [2, 1, 3],
#   [2, 3, 1],
#   [3, 1, 2],
#   [3, 2, 1]
# ]
# Explanation: Given an array, return all the possible permutations.
# Example 2:
# Input: arr = [0, 1]
# Output:
# [
#   [0, 1],
#   [1, 0]
# ]
# Explanation: Given an array, return all the possible permutations.

# Time Complexity: O(N! X N)

# Space Complexity: O(1)


class Solution:
    def per(self,idx,ans,nums):
        if idx == len(nums):
            ds = []
            for i in nums:
                ds.append(i)
            ans.append(ds)
            return
        for i in range(idx, len(nums)):
            nums[idx],nums[i] = nums[i],nums[idx]
            self.per(idx+1,ans,nums)
            nums[idx],nums[i] = nums[i],nums[idx]
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.per(0,ans,nums)
        return ans
