import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = sys.maxint
        profit = 0
        for i in prices:
            min_price = min(min_price,i)
            profit = max(i-min_price,profit)
        return profit
                
                