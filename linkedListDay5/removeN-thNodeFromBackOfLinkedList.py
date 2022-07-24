# Problem Statement: Given a linked list, and a number N. Find the Nth node from the end of this linked list and delete it. Return the head of the new modified linked list.
# Example 1 : 
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Input: head = [7,6,9,4,13,2,8], n = 6
# Output: [7,9,4,13,2,8]

# Time Complexity: O(N)
# Space Complexity: O(1)

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head
    slow = dummy
    fast = dummy
    for i in range(n):
        fast = fast.next
    while fast and fastnext:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next