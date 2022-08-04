# Problem Statement: There is one meeting room in a firm. You are given two arrays, start and end each of size N.For an index ‘i’, start[i] denotes the starting time of the ith meeting while end[i]  will denote the ending time of the ith meeting. Find the maximum number of meetings that can be accommodated if only one meeting can happen in the room at a  particular time. Print the order in which these meetings will be performed.

# Example:
# Input:  N = 6,  start[] = {1,3,0,5,8,5}, end[] =  {2,4,5,7,9,9}

# Output: 1 2 4 5
# Explanation: See the figure for a better understanding. 

# Time Complexity: O(n) to iterate through every position and insert them in a data structure. O(n log n)  to sort the data structure in ascending order of end time. O(n)  to iterate through the positions and check which meeting can be performed.
# Overall : O(n) +O(n log n) + O(n) ~O(n log n)
# Space Complexity: O(n)  since we used an additional data structure for storing the start time, end time, and meeting no.

def maximumMeetings(self,n,start,end):
    ds = []
    for i in range(n):
        ds.append([end[i], start[i]])
    
    ds.sort(key = lambda i:i[0])
    e = ds[0][0]
    count = 1
    for i in range(1,n):
        if ds[i][1] > e:
            count += 1
            e = ds[i][0]
    return count