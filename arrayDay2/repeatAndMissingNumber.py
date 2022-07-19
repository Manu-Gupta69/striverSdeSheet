# Problem Statement: You are given a read-only array of N integers with values also in the range [1, N] both inclusive. Each integer appears exactly once except A which appears twice and B which is missing. The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.
# Example 1:
# Input Format:  array[] = {3,1,2,5,3}
# Result: {3,4)
# Explanation: A = 3 , B = 4 
# Since 3 is appearing twice and 4 is missing
# Example 2:
# Input Format: array[] = {3,1,2,5,4,6,7,5}
# Result: {5,8)
# Explanation: A = 5 , B = 8 
# Since 5 is appearing twice and 8 is missing

# Time Complexity: O(N)
# Space Complexity: O(N) As we are making new substitute array

def repeatedNumber(self, A):
    ans=[]
    sum1=sum(A)
    n=len(A)
    s=n*(n+1)//2
    A=list(set(A))
    sum2=sum(A)
    rep_num=sum1-sum2
    ans.append(rep_num)
    ans.append(s-sum2)
    return ans