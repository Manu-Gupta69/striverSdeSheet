# Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.
# Examples:

# Example 1: 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k
# Example 2:

# Input: nums=[-1,0,1,0]
# Output: Output: [[-1,0,1],[-1,1,0]]
# Explanation: Out of all possible unique triplets possible, [-1,0,1] and [-1,1,0] satisfy the condition of summing up to zero with i!=j!=k


# Time Complexity : O(n^2)  

# Space Complexity : O(3*k)  // k is the no.of triplets. 


def threeSum(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    ans = []
    
    for i in range(n-2):
        if i == 0 or i > 0 and nums[i] != nums[i - 1]:
            low = i+1 
            hi = n-1
            s = 0-nums[i]
            while low < hi:
                if nums[low] + nums[hi] == s:
                    temp = []
                    temp.append(nums[i])
                    temp.append(nums[low])
                    temp.append(nums[hi])
                    ans.append(temp)
                    while low < hi and nums[low] == nums[low + 1]:
                        low += 1
                    while low < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    low += 1
                    hi -= 1
                elif nums[low] + nums[hi] > s:
                    hi -= 1
                else:
                    low += 1
    return ans

    
