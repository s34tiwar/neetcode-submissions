from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for i in range(len(nums)):
            map[nums[i]] += 1
        arr = []  
        for key, value in map.items():
            arr.append([value, key])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
