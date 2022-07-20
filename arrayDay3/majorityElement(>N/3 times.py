# Problem Statement: Given an array of N integers. Find the elements that appear more than N/3 times in the array. If no such element exists, return an empty vector.
# Example 1:
# Input: N = 5, array[] = {1,2,2,3,2}
# Ouput: 2
# Explanation: Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.Therefore, the count of 2 is greater than N/3 times. Hence, 2 is the answer.
# Example 2:
# Input:  N = 6, array[] = {11,33,33,11,33,11}
# Output: 11 33
# Explanation: Here we can see that the Count(11) = 3 and Count(33) = 3. Therefore, the count of both 11 and 33 is greater than N/3 times. Hence, 11 and 33 is the answer.

# Time Complexity: O(n)
# Space Complexity: O(1)

def majorityElement(self, nums: List[int]) -> List[int]:
    n = len(nums)
    nums1 = -1
    nums2 = -2
    c1 = 0
    c2 = 0
    for i in nums:
        if i == nums1:
            c1 += 1
        elif i == nums2:
            c2 += 1
        elif c1 == 0:
            nums1 = i
            c1 = 1
        elif c2 == 0:
            nums2 = i
            c2 = 1
        else:
            c1 -= 1
            c2 -= 1
    count1 = 0
    count2 = 0
    ans = []
    for i in nums:
        if i == nums1:
            count1 += 1
        if i == nums2:
            count2 += 1
    if count1 > n/3:
        ans.append(nums1)
    if count2 > n/3:
        ans.append(nums2)
    return ans