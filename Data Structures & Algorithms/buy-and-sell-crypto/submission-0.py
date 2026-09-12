class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range(len(prices)):
            j = i + 1
            profit=0
            while j < len(prices):
                profit = max(profit,prices[j]-prices[i])
                j+=1
            maximum = max(profit,maximum)
        return maximum
