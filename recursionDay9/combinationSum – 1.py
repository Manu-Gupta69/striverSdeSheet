# Problem Statement: 
# Given an array of distinct integers and a target, you have to return the list of all unique combinations where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from the given array an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
# Examples:
# Example 1:
# Input: array = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
#              7 is a candidate, and 7 = 7.
#              These are the only two combinations.
# Example 2:
# Input: array = [2], target = 1
# Output: []
# Explaination: No combination is possible.

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    def combination(idx,target,ds):
        if idx == len(candidates):
            if target == 0:
                res.append(ds[::])
            return
        if candidates[idx] <= target:
            ds.append(candidates[idx])
            combination(idx,target-candidates[idx],ds)
            ds.pop()
        combination(idx+1,target,ds)
    res = []
    combination(0,target,[])
    return res