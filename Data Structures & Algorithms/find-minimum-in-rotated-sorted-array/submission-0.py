class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # min is to the right of mid 
                left = mid + 1
            else:
                # min could be mid or left 
                right = mid 
        return nums[left]