import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap,-nums[i])
        curr = 0
        while k > 0:
            curr = heapq.heappop(heap)
            k -= 1
        return -curr
