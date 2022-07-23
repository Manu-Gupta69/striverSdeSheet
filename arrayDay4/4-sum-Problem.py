# 4 Sum | Find Quads that add up to a target value
# Problem Statement: Given an array of N integers, your task is to find unique quads that add up to give a target value. In short, you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given target.
# Pre-req: Binary Search and 2-sum problem
# Note:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# arr[a] + arr[b] + arr[c] + arr[d] == target
# Example 1:
# Input Format: arr[] = [1,0,-1,0,-2,2], target = 0
# Result: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Explanation: We have to find unique quadruplets from 
# the array such that the sum of those elements is 
# equal to the target sum given that is 0. 
# The result obtained is such that the sum of the 
# quadruplets yields 0.
# Example 2:
# Input Format: arr[] = [4,3,3,4,4,2,1,2,1,1], target = 9
# Result: [[1,1,3,4],[1,2,2,4],[1,2,3,3]]
# # Solution:
# Time Complexity: O(N log N + N³ logN)
# Reason: Sorting the array takes N log N and three nested loops will be taking N³ and for binary search, it takes another log N.
# Space Complexity: O(M * 4), where M is the number of quads

def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        nums.sort()
        arr = []
        n = len(nums)
        
        for i in range(0,n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                l = n-1
                
                while k < l:
                    sum_ = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if sum_ < target:
                        k += 1
                    
                    elif sum_ > target:
                        l -= 1
                        
                    else:
                        if [nums[i], nums[j], nums[k], nums[l]] not in arr:
                            arr.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        
        return arr