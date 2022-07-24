# Problem Statement: Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.
# Examples:
# Input Format: 
# ( Pointer / Access to the head of a Linked list )
# head = [1,2,3,4,5]
# Result: [3,4,5]
# ( As we will return the middle of Linked list the further linked list will be still available )
# Explanation: The middle node of the list is node 3 as in the below image.

# Time Complexity: O(N)
# Space Complexity: O(1)

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
