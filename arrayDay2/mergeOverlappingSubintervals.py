# Problem Statement: Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.
# Examples
# Example 1: 
# Input: intervals=[[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6]
#  intervals.
# Example 2:
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6] intervals

# Time Complexity: O(NlogN) + O(N). O(NlogN) for sorting and O(N) for traversing through the array.
# Space Complexity: O(N) to return the answer of the merged intervals.



def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key = lambda i : i[0])
    output = [intervals[0]]
    for start, end in intervals[1:]:
        lastEnd = output[-1][1]
        if lastEnd > start:
            output[-1][1] = max(output[-1][1],end)
        else:
            output.append([start,end])
    return output