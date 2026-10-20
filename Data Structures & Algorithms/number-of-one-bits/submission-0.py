class Solution:
    def hammingWeight(self, n: int) -> int:
        x = n 
        res = 0
        base = 1
        count = 0
        while x > 0:
            rem = x % 2 
            if rem == 1:
                count += 1
            res += base*rem 
            x = x// 2 
            base *= 10
        return count