# Problem Statement: Given the heads of two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# Examples:
# Input Format: 
# (Pointer/Access to the head of the two linked lists)
# num1  = 342, num2 = 564
# l1 = [2,4,3]
# l2 = [5,6,4]
# Result: sum = 807; L = [7,0,8]
# Explanation: Since the digits are stored in reverse order, reverse the numbers first to get the or original number and then add them as → 342 + 465 = 807.

# Time Complexity: O(max(m,n)). Assume that m and n represent the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.
# Space Complexity: O(max(m,n)). The length of the new list is at most max(m,n)+1.

from socket import CAN_RTR_FLAG


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    temp = dummy
    carry = 0
    while l1 or l2 or carry:
        sums = 0
        if l1:
            sums += l1.val
            l1 = l1.next
        if l2:
            sums += l2.val
            l2 = l2.next
        sums += carry
        carry = sums//10
        node = ListNode(sums%10)
        temp.next = node
        temp = temp.next
    return dummy.next