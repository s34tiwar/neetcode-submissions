class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i):
            # base case: we made decision for each number 
            if i == len(nums):
                return res.append(curr.copy())
                return 
            # choice 1: include 
            curr.append(nums[i])
            dfs(i + 1)
            # undo 
            curr.pop()
            # choice 2: don't include nums[i] 
            dfs(i + 1)
        dfs(0)
        return res
