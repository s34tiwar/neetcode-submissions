class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        curr = []
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        def bactracking(i):
            if i == len(digits):
                res.append("".join(curr))
                return 
            digit = digits[i]
            for letter in mapping[digit]:
                curr.append(letter)
                bactracking(i + 1)
                curr.pop()
        bactracking(0)
        return res


