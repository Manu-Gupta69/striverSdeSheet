def maxSubArray(self, nums: List[int]) -> int:
    maximum = nums[0]
    currentMax = 0
    for i in nums:
        currentMax += i 
        if currentMax > maximum:
            maximum = currentMax
        elif currentMax < 0:
            currentMax = 0
    return maximum