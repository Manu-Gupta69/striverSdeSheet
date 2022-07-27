# Problem Statement: Given the head of a singly linked list, return true if it is a palindrome.

# Examples:
# Example 1:
# Input: head = [1,2,3,3,2,1] 
# Output:
#  true
# Explanation: If we read elements from left to right, we get [1,2,3,3,2,1]. When we read elements from right to left, we get [1,2,3,3,2,1]. Both ways list remains same and hence, the given linked list is palindrome.
# Example 2:
# Input:
#  head = [1,2]
# Output:
#  false
# Explanation: When we read elements from left to right, we get [1,2]. Reading from right to left, we get a list as [2,1]. Both are different and hence, the given linked list is not palindrome.

# Time Complexity: O(N/2)+O(N/2)+O(N/2)

# Reason: O(N/2) for finding the middle element, reversing the list from the middle element, and traversing again to find palindrome respectively.

# Space Complexity: O(1)

def isPalindrome(self, head: Optional[ListNode]) -> bool:
    def reverse(head):
            prev = None
            current = head
            forward = head
            while current:
                forward = current.next
                current.next = prev
                prev = current
                current = forward
            return prev
        
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow = reverse(slow)

    while slow:
        if slow.val != head.val:
            return False
        slow = slow.next
        head = head.next
    return True