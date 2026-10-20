class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            total = nums[j] + nums[i]
            if total == target:
                return [i + 1, j + 1]
            elif total < target:
                i += 1
            else:
                j -= 1
        return []

