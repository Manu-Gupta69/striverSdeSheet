def sortColors(self, nums: List[int]) -> None:
    n = len(nums)-1
    start = 0
    end = n
    mid = 0
    while mid < end:
        if nums[mid] == 0:
            nums[start],nums[mid] = nums[mid],nums[start]
            nums += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid],nums[end] = nums[end],nums[mid]
            end -= 1
        else:
            mid += 1

#  Time Complexity = O(N)
# Space Complexity =  O(1)


