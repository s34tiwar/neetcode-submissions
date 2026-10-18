"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        rooms = []

        for interval in intervals:
            start = interval.start
            end = interval.end

            # Earliest-ending room is free
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)

            # Use/reuse a room until current meeting ends
            heapq.heappush(rooms, end)

        return len(rooms)

# class Solution:
#     def minMeetingRooms(self, intervals: List[Interval]) -> int:
#         intervals.sort(key = lambda x: x.start)
#         rooms = [] # each value = when room becomes free
#         for i in intervals:
#             start = i.start 
#             end = i.end 
#             room_found = False
#             for r in range(len(rooms)):
#                 if start >= rooms[r]:
#                     rooms[r] = end
#                     room_found = True
#                     break
#             if not room_found:
#                 rooms.append(end)
#         return len(rooms)