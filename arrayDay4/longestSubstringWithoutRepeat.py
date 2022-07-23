# Problem Statement: Given a String, find the length of longest substring without any repeating character.
# Examples:
# Example 1:
# Input: s = ”abcabcbb”
# Output: 3
# Explanation: The answer is abc with length of 3.
# Example 2:
# Input: s = ”bbbbb”
# Output: 1
# Explanation: The answer is b with length of 1 units.


# Time Complexity: O( N )
# Space Complexity: O(N) where N represents the size of HashSet where we are storing our elements

def lengthOfLongestSubstring(self, s: str) -> int:
    hashSet = {}
    length = 0
    l = 0
    r = 0
    while r < len(s):
        if s[r] not in hashSet:
            hashSet[s[r]] = r
        else:
            l = max(l,hashSet[s[r]]+1)
            hashSet[s[r]] = r
        r += 1
        length = max(length,r-l)
    return length
