# Problem Statement: Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
# (i) a next pointer to the next node,
# (ii) a bottom pointer to a linked list where this node is head.
# Each of the sub-linked-list is in sorted order.
# Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 
# Note: The flattened list will be printed using the bottom pointer instead of the next pointer.
# Examples:

# Example 1:
# Input:
# Number of head nodes = 4
# Array holding length of each list with head and bottom = [4,2,3,4]
# Elements of entire linked list = [5,7,8,30,10,20,19,22,50,28,35,40,45]

# Output:
#  Flattened list = [5,7,8,10,19,20,22,28,30,35,40,45,50]
# Explanation:
#  Flattened list is the linked list consisting entire elements of the given list in sorted order
# Example 2:
# Input:
# Number of head nodes = 4
# Array holding length of each list with head and bottom = [4,1,3,1]
# Elements of entire linked list = [5,7,8,30,10,19,22,50,28]

# Output:
#  Flattened list = [5,7,8,10,19,22,28,30,50]
# Explanation:
#  Flattened list is the linked list consisting entire elements of the given list in sorted order

# Time Complexity: O(N), where N is the total number of nodes present
# Reason: We are visiting all the nodes present in the given list.

# Space Complexity: O(1)
# Reason: We are not creating new nodes or using any other data structure.

def flatten(root):
    def merge(a,b):
        temp = Node(0)
        res = temp

        while a and b:
            if a.data < b.data:
                temp.bottom = a
                temp = temp.bottom
                a  = a.bottom
            else:
                temp.bottom = b
                temp = temp.bottom
                b = b.bottom
        if a:
            temp.bottom = a
            temp = temp.bottom
            a = a.bottom
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom

        return res.bottom
    if not root or not root.next:
        return root
    root.next = flatten(root.next)
    root = merge(root,root.next)
    return root