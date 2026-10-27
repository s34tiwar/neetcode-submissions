class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(curr_arrr, curr_sum, i):
            if curr_sum == target:
                res.append(curr_arrr.copy())
                return 
            for j in range(i, len(candidates)):
                # skip dupcilate 
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if curr_sum + candidates[j] > target:
                    break
                # make a choice 
                curr_arrr.append(candidates[j])
                # explore - start from j + 1 to avoid choosing name elements
                backtrack(curr_arrr, curr_sum + candidates[j], j + 1)
                # undo
                curr_arrr.pop()
        backtrack([], 0, 0)
        return res
            