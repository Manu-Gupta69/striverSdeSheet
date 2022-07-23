# Problem Statement: Given an array of numbers, you need to return the count of reverse pairs. Reverse Pairs are those pairs where i<j and arr[i]>2*arr[j].
# Example 1:
# Input: N = 5, array[] = {1,3,2,3,1)
# Output: 2 
# Explanation: The pairs are (3, 1) and (3, 1) as from both the pairs the condition arr[i] > 2*arr[j] is satisfied.
# Example 2:
# Input: N = 4, array[] = {3,2,1,4}
# Output: 1
# Explaination: There is only 1 pair  ( 3 , 1 ) that satisfy the condition arr[i] > 2*arr[j]

# Time Complexity : O( N log N ) + O (N) + O (N)   
# Reason : O(N) – Merge operation , O(N) – counting operation ( at each iteration of i , j doesn’t start from 0 . Both of them move linearly ) 
# Space Complexity : O(N) 
# Reason : O(N) – Temporary vector

def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        
        def mergeSort(nums):
            if len(nums) < 2: return nums
            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            
            # finding pair
            a = b = 0
            while a < len(left) and b < len(right):
                if left[a] > 2 * right[b]:
                    self.count += (len(left) - a)
                    b += 1
                else: a += 1
                    
            a = b = 0
            arr = []
            # merging the sorted arrays
            while a < len(left) or b < len(right):
                if a < len(left) and (b >= len(right) or left[a] < right[b]):
                    arr.append(left[a])
                    a += 1
                else:
                    arr.append(right[b])
                    b += 1
            return arr
        
        arr = mergeSort(nums)
        return self.count