class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(curr):
            # reached exactly the top, count it
            if curr == n:
                return 1
            # went past the top 
            if curr > n:
                return 0
            
            # already sloved this postion before
            if curr in memo:
                return memo[curr]
            
            # take 2 step or two 
            # no of ways from here = ways if I have 1 step + ways if I take 2 stps 
            memo[curr] = dfs(curr + 1) + dfs(curr + 2)
            return memo[curr]
        return dfs(0)













# Brute force DFS 
        # def dfs(curr):
        #     if curr == n:
        #         return 1
        #     if curr > n:
        #         return 0
            
        #     return dfs(curr + 1) + dfs(curr + 2)
        # return dfs(0)