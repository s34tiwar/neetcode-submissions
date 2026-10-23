class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return amount + 1
            if remaining in memo:
                return memo[remaining]
            minimum = amount + 1
            for coin in coins:
                # use the coin, slove the smaller remaining ampunt 
                result = dfs(remaining - coin)
                minimum = min(minimum, 1 + result)
            memo[remaining] = minimum
            return minimum
        answer = dfs(amount)
        if answer > amount:
            return -1
        return answer