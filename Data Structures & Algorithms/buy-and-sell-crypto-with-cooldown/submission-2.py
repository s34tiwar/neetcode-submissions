class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, can_buy):
            if i >= len(prices):
                return 0
            if (i, can_buy) in memo:
                return memo[(i,can_buy)]
            if can_buy:
                # buy today or skip 
                memo[(i,can_buy)] = max(-prices[i] + dfs(i + 1, False), dfs(i+1, True))
            else:
                # sell today or keep holding
                memo[(i,can_buy)] =  max(prices[i] + dfs(i + 2, True), dfs(i+1, False))
            return memo[(i, can_buy)]
        return dfs(0, True)