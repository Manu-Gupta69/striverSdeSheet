# Problem Statement: Given the head of a linked list, rotate the list to the right by k places.
# Examples:

# Example 1:
# Input:
# 	head = [1,2,3,4,5] 
# 	k = 2
# Output:
#  head = [4,5,1,2,3]
# Explanation:
#  We have to rotate the list to the right twice.

# Example 2:
# Input:
# 	head = [1,2,3]
# 	k = 4
# Output:
# head = [3,1,2]
# Explanation:

from socket import has_dualstack_ipv6


def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    cur = head
    length = 1
    while cur.next:
        cur = cur.next
        length += 1
    cur.next = head
    k =  k % length
    k = length - k
    while k and cur:
        cur = cur.next
        k -= 1
    head = cur.next
    cur.next = None
    return head
