class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0
        for num in nums:
            curr = max(prev1, prev2 + num)   # prev1 = skip it, prev2 + num = rob this house 
            prev2  = prev1
            prev1 = curr
        return prev1
    # we choose to rob the current house, we add its money to prev2, not prev1 to make sure not adjcanet 
