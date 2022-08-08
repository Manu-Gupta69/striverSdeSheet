# Problem Statement: The weight of N items and their corresponding values are given. We have to put these items in a knapsack of weight W such that the total value obtained is maximized.
# Note: We can either take the item as a whole or break it into smaller units.
# Example:
# Input: N = 3, W = 50, values[] = {100,60,120}, weight[] = {20,10,30}.
# Output: 240.00
# Explanation: The first and second items  are taken as a whole  while only 20 units of the third item is taken. Total value = 100 + 60 + 80 = 240.00

# Time Complexity: O(n log n + n). O(n log n) to sort the items and O(n) to iterate through all the items for calculating the answer.
# Space Complexity: O(1), no additional data structure has been used.

def fractionalknapsack(self, W,Items,n):
    Items.sort(key = lambda x: x.value/x.weight, reverse = True)

    value = 0
    for item in Items:
        if item.weight <= W:
            W -= item.weight
            value += item.value
        else:
            value += (item.value/item.weight)*W
            break
    return value