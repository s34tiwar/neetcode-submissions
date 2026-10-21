class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        #The fastest useful speed we ever need to consider
        # is the size of the largest pile.
        right = max(piles)
        answer = right
        while left <= right:
            mid = (left + right) // 2
            k = mid
            hours = 0
            # calculate the hours this k piles will take 
            for pile in piles:
                hour_per_pile = (pile + k - 1) // k
                hours += hour_per_pile
            # k works, but maybe a smaller speed also works
            if hours <= h:
                answer = k
                right = mid - 1
            else:
                left = mid + 1
        return answer