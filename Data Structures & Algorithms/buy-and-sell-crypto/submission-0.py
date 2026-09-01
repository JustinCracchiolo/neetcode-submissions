class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0

        minSell = prices[0]

        for p in prices:
            minSell = min(minSell, p)
            maxProfit = max(maxProfit, p - minSell)

        return maxProfit