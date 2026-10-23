class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(r,c) -> int:
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1):
                return 0
            # mark visited
            grid[r][c] = 0
            # current cell contrubted area 1 
            area = 1

            area += dfs(r + 1, c)
            area += dfs(r-1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    max_area = max(max_area, area)
        return max_area