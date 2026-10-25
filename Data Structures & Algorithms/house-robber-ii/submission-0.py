class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # 
        def rob_line(arr):
            prev1 = 0
            prev2 = 0
            for num in arr:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr
            return prev1
        
        return max(rob_line(nums[0:len(nums) - 1]),rob_line(nums[1:len(nums)]))
