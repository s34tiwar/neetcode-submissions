from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        left = 0
        right = len(s1) - 1
        while right < len(s2):
            curr_string = s2[left:right + 1]
            s2_map = Counter(curr_string)
            if s1_map == s2_map:
                return True
            left += 1
            right += 1
        return False