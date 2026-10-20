class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0 : 1}
        prefix = 0
        res = 0
        for num in nums:
            prefix += num
            rem = prefix - k
            if rem in freq:
                times_occured = freq[rem]
                res += times_occured 
            freq[prefix] = freq.get(prefix, 0) + 1
        return res
            
