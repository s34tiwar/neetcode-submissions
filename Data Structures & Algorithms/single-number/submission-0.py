from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        for key, value in map.items():
            if value == 1:
                return key
        return