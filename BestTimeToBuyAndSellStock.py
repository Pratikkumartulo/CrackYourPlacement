class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyat = prices[0]
        profit=0
        for i in range(len(prices)):
            buyat = min(buyat,prices[i])
            if buyat<prices[i]:
                profit=max(profit,prices[i]-buyat)
        return profit