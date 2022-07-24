# Problem Statement: Given two singly linked lists that are sorted in increasing order of node values, merge two sorted linked lists and return them as a sorted list. The list should be made by splicing together the nodes of the first two lists.
# Example 1:
# Input Format :
# l1 = {3,7,10}, l2 = {1,2,5,8,10}
# Output :
# {1,2,3,5,7,8,10,10}

# Time Complexity :
# We are still traversing both lists entirely in the worst-case scenario. So, it remains the same as O(N+M) where N is the number of nodes in list 1 and M is the number of nodes in list 2.
# Space Complexity :
# We are using the same lists just changing links to create our desired list. So no extra space is used. Hence, its space complexity is O(1). 

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2:
        return list1
    if list1 and not list2:
        return list1
    if list2 and not list1:
        return list2
    if list1.val > list2.val:
        l1 = list2
        l2 = list1
    else:
        l1 = list1
        l2 = list2
    res = l1
    while l1 and l2:
        while l1.next and l1.next.val < l2.val:
            l1 = l1.next
        l1.next,l2 = l2,l1.next
        l1 = l1.next
    return res