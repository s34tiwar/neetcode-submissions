class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        i = 0
        longest = 0
        for j in range(len(s)):
            while s[j] in res:
                res.remove(s[i])
                i += 1
            res.add(s[j])
            longest = max(longest, j - i + 1)
        return longest 

            
            