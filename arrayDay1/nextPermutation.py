def nextPermutation(self, nums: List[int]) -> None:
    n = len(nums)
    pointer = n-2
    
    while pointer >= 0 and nums[pointer] >= nums[pointer+1]:
        pointer -= 1
    
    if pointer == -1:
        return nums.reverse()
    
    for i in range(n-1, pointer, -1):
        if nums[pointer] < nums[i]:
            nums[pointer],nums[i] = nums[i],nums[pointer]
            break
    nums[pointer+1:] = reversed(nums[pointer+1:])

# Time Complexity = O(N) For the first iteration backward, the second interaction backward and reversal at the end takes O(N) for each, where N is the number of elements in the input array. This sums up to 3*O(N) which is approximately.
# Space Complexity = O(1) Since no extra storage is required.

