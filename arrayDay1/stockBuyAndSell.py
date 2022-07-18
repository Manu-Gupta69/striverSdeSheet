def maxProfit(self, prices: List[int]) -> int:
    maxProfit = -10000
    minPrice = 10000
    for i in prices:
        minPrice = min(minPrice,i)
        maxProfit = max(maxProfit,i - minPrice)
    return maxProfit
        
# Time Complexity = O(N)
# Space Complexity = O(1)