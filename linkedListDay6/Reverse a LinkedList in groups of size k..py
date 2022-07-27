# Problem Statement: Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# Note: Also check this article to reverse a linked list
# Examples:
# Example 1:
# Input:
#  head = [1,2,3,4,5,6,7,8] k=3
# Output:
#  head = [3,2,1,6,5,4,7,8]
# Explanation:
# Example 2:
# Input:
#  head = [1,2,3,4,5,6,7,8] k=2
# Output:
#  head = [2,1,4,3,6,5,8,7]
# Explanation:


def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head
    cur = dummy
    prev = dummy
    forward = dummy
    length = 0
    while cur:
        length += 1
        cur = cur.next
    
    while length > k:
        cur = prev.next
        forward = cur.next
        for i in range(1,k):
            cur.next = forward.next
            forward.next = prev.next
            prev.next = forward
            forward = cur.next
        prev = cur
        length -= k
    return dummy.next