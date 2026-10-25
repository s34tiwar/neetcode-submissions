class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index_stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            # if first time 
            if not index_stack:
                index_stack.append(i)
            else:
                # check every 
                while index_stack and temperatures[index_stack[-1]] < temperatures[i]:
                    index = index_stack.pop()
                    # no of days waited is curr_day - previous day 
                    res[index] = i - index
            index_stack.append(i)
        return res