class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        bestProfit = 0

        for i in range(1, len(prices)):
            buy = prices[l]
            sell = prices[i]
            if sell < buy:
                l = i
            profit = sell - buy
            bestProfit = max(profit, bestProfit)

        return bestProfit

        