# Problem Statement: Given an array of integers that may contain duplicates the task is to return all possible subsets. Return only unique subsets and they can be in any order.

# Examples:
# Example 1:
# Input: array[] = [1,2,2]
# Output: [ [ ],[1],[1,2],[1,2,2],[2],[2,2] ]
# Explanation: We can have subsets ranging from  length 0 to 3. which are listed above. Also the subset [1,2] appears twice but is printed only once as we require only unique subsets.
# Input: array[] = [1]
# Output: [ [ ], [1] ]
# Explanation: Only two unique subsets are available

def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    def subset(idx,ds):
        result.append(ds[::])
        for i in range(idx,len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            ds.append(nums[i])
            subset(i+1,ds)
            ds.pop()
    result = []
    subset(0,[])
    return result
        