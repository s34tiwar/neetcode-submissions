class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        temp = abs(x)
        res = 0
        count = 1
        while temp > 0:
            temp = temp // 10
            count *= 10
        temp = abs(x)
        base = count // 10
        while temp:
            rem = temp % 10
            res +=  rem * base
            base = base // 10
            temp = temp // 10
        if neg:
            res = res * -1
        if res < - (2**31) or res > 2**31 - 1:
            return 0
        return res
