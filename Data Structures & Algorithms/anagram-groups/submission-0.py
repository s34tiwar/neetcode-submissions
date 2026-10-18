from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for s in strs:
            s_sorted = ''.join(sorted(s))
            map[s_sorted].append(s)
        return list(map.values())
        