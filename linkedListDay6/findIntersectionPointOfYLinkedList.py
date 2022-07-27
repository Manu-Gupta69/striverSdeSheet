# Problem Statement: Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Examples:
# Example 1:
# Input:
# List 1 = [1,3,1,2,4], List 2 = [3,2,4]
# Output:
# 2
# Explanation: Here, both lists intersecting nodes start from node 2.

# Example 2:
# Input:
#  List1 = [1,2,7], List 2 = [2,8,1]
# Output:
#  Null
# Explanation: Here, both lists do not intersect and thus no intersection node is present.

# Time Complexity: O(2*max(length of list1,length of list2))
# Reason: Uses the same concept of difference of lengths of two lists.
# Space Complexity: O(1)


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    d1 = headA
    d2 = headB
    while d1 != d2:
        d1 = d1.next if d1 else headB
        d2 = d2.next if d2 else headA
    return d1