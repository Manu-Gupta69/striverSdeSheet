# Problem Statement: Given an array of non-negative integers representation elevation of ground. Your task is to find the water that can be trapped after rain.
# Examples:
# Example 1:
# Input: height= [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: As seen from the diagram 1+1+2+1+1=6 unit of water can be trapped

# Example 2:
# Input:  [4,2,0,3,2,5]
# Output:9

# Time Complexity: O(N) because we are using 2 pointer approach.

# Space Complexity: O(1) because we are not using anything extra.

def trap(self, height: List[int]) -> int:
    n = len(height)
    left = 0
    right = n-1
    leftMax = rightMax = 0
    res = 0
    while left <= right:
        if height[left] <= height[right]:
            if height[left] > leftMax:
                leftMax = height[left]
            else:
                res += leftMax - height[left]
            left += 1
        else:
            if height[right] > rightMax:
                rightMax = height[right]
            else:
                res += rightMax - height[right]
            right -= 1
    return res