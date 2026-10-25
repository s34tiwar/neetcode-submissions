class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # both start as first number
        curr_max = nums[0]
        curr_min = nums[0]
        # overall bets product seen so far
        result = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            # save old values bcz both new values depend on previous curr_max and curr_min 
            prev_max = curr_max
            prev_min = curr_min
            # current subarray can 1. fresh start x, 2. extend previous max, 3. extend previous min
            curr_max = max(
                x, 
                prev_max * x, 
                prev_min * x
            )

            curr_min = min(
                x, 
                prev_min * x, 
                prev_max * x
            )
            # upatde global answer 
            result = max(result, curr_max, curr_min)
        return result