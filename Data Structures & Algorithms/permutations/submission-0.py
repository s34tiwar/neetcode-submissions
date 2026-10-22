class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        used = set()
        def backtracking():
            # base case 
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 
            # try every number
            for num in nums:
                if num in used:
                    continue
                # choose 
                curr.append(num)
                used.add(num)
                # explore
                backtracking()
                # undo 
                curr.pop()
                used.remove(num)
        backtracking()
        return res

