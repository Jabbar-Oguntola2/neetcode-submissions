class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        maxprof = 0
        l, r = 0, 1
        while r < len(prices):
            prof = prices[r] - prices[l]
            maxprof = max(maxprof, prof)
            if prices[l] <= prices[r]:
                r += 1
            else:
                l += 1
        
        return maxprof
