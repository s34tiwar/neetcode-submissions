class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n + 1):
            x = i
            base = 1
            rem = 0 
            count = 0
            while x > 0:
                r = x % 2
                rem += base*r 
                base *= 10 
                if r == 1:
                    count += 1
                x  = x // 2  
            arr.append(count)
        return arr
            