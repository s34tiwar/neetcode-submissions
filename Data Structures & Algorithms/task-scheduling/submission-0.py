import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []       # max heap of the freq of all symbol, 
        for count in freq.values():
            heapq.heappush(heap, -count)
        cooldown = deque()
        time = 0
        while heap or cooldown:
            time += 1
            if heap:
                count = heapq.heappop(heap)
                count += 1
              # if there is still task left 
                if count < 0:
                    cooldown.append([count, time + n])
            # check if any task cooled down 
            if cooldown and time == cooldown[0][1]:
                count, ready_time = cooldown.popleft()
                heapq.heappush(heap, count)
        return time


