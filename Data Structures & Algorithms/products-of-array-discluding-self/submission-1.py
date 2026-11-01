class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        # product of eveything from left 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # now start from back 
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res