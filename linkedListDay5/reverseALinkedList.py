# Problem Statement: Given the head of a singly linked list, write a program to reverse the linked list, and return the head pointer to the reversed list.
# Examples:
# Input Format: 
# head = [3,6,8,10]
# This means the given linked list is 3->6->8->10 with head pointer at node 3.
# Result:
# Output = [10,6,8,3]
# This means, after reversal, the list should be 10->6->8->3 with the head pointer at node 10.

# Time Complexity:
# Since we are iterating only once through the list and achieving reversed list. Thus, the time complexity is O(N) where N is the number of nodes present in the list.
# Space Complexity:
# To perform given tasks, no external spaces are used except three-pointers. So, space complexity is O(1).



def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head
    forward = head
    while current:
        forward =  current.next
        current.next = prev
        prev = current 
        current = forward
    return prev