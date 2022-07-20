# Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. You may consider that such an element always exists in the array.
# Example 1:
# Input Format: N = 3, nums[] = {3,2,3}
# Result: 3
# Explanation: When we just count the occurrences of each number and compare with half of the size of the array, you will get 3 for the above solution. 

# Time Complexity: O(N)
# Space Complexity: O(1)



def majorityElement(self, nums: List[int]) -> int:
    count = 0
    element = 0
    for i in nums:
        if count == 0:
            element = i
        if i == element:
            count += 1
        else:
            count -= 1
    return element