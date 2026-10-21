class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check start and end points for each list if the target lies there, so binary seach in that list 
        for row in matrix:
            if row[0] <= target <= row[-1]:
                left = 0
                right = len(row) - 1
                while left <= right:
                    mid = (right + left) // 2
                    if row[mid] == target:
                        return True
                    if row[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False
