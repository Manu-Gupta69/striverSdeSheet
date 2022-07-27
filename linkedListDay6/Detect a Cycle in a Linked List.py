# Problem Statement: Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Return true if there is a cycle in the linked list. Otherwise, return false.
# Examples:
# Example 1:
# Input:
#  Head = [1,2,3,4]
# Output:
#  true
# Explanation: Here, we can see that we can reach node at position 1 again by following the next pointer. Thus, we return true for this case.
# Example 2:
# Input:
#  Head = [1,2,3,4]
# Output:
#  false
# Explanation: Neither of the nodes present in the given list can be visited again by following the next pointer. Hence, no loop exists. Thus, we return false.
# Time Complexity: O(N)
# Reason: In the worst case, all the nodes of the list are visited.
# Space Complexity: O(1)
# Reason: No extra data structure is used.

def hasCycle(self, head: Optional[ListNode]) -> bool:
    if not head:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        if slow == fast:
            return True
    return False