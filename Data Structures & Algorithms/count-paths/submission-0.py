class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(r,c):
            # base case found one path 
            if r == m - 1 and c == n - 1:
                return 1
            # make sure to be in boundary 
            if r >= m or r < 0 or c >= n or c < 0:
                return 0
            # check if the result already in memo
            if (r,c) in memo:
                return memo[(r,c)]

            # explore
            memo[(r,c)] = dfs(r, c + 1) + dfs(r+1, c)
            return memo[(r,c)]
        return dfs(0,0)