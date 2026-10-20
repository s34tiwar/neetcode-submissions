class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes = []
        res = []
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res.append(str(sz))
            res.append(",")
        res.append("#")
            # extend(x)  → add EACH item inside x
            # ["3", ",", "4", "#", "cat", "dog"] 
            # while append(x)  → add x as ONE item
        res.extend(strs)
        return ''.join(res)     # make it a whole one string 

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        size = []
        res = []
        i = 0
        while s[i] != "#":
            j = i
            while s[j] != ",":
                j += 1
            size.append(int(s[i:j]))
            i = j + 1
        i += 1
        for sz in size:
            res.append(s[i:i + sz])
            i += sz
        return res        
