class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(i, curr_arr, curr_sum):
            # base case
            if curr_sum == target:
                res.append(curr_arr.copy())
            # try each possible choice 
            for j in range(i, len(nums)):
                if curr_sum + nums[j] > target:
                    continue
                # make choice 
                curr_arr.append(nums[j])
                # explore
                backtracking(j, curr_arr, curr_sum + nums[j])
                # undo choice 
                curr_arr.pop()
        backtracking(0, [], 0)
        return res
