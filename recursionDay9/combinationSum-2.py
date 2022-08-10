# Problem Statement: Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.
# Examples:
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]]
# Explanation: These are the unique combinations whose sum is equal to target. 
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: [[1,2,2],[5]]
# Explanation: These are the unique combinations whose sum is equal to target.
# Time Complexity:O(2^n*k)
# Reason: Assume if all the elements in the array are unique then the no. of subsequence you will get will be O(2^n). we also add the ds to our ans when we reach the base case that will take “k”//average space for the ds.
# Space Complexity:O(k*x)

from tarfile import _Bz2ReadableFileobj


def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    def combinantion(idx,target,ds):
        if target == 0:
            res.append(ds[::])
            return
        for i in range(idx,len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            ds.append(candidates[i])
            combinantion(i+1,target-candidates[i],ds)
            ds.pop()
    candidates.sort()
    res = []
    combinantion(0,target,[])
    return res