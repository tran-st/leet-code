from heapq import *
import interval


def min_meeting_rooms(intervals):
    if not intervals or len(intervals) == 0:
        return 0

    count, result = 0, 0
    i, j = 0, 0
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    while i < len(intervals):
        if start[i] < end[j]: # Meeting not ended, increment
            i += 1
            count += 1
            result = max(result, count)
        else:
            j += 1
            count -= 1
    
    return result

"""
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)

Approach:

[(0,30),(30,35),(35,40)]
         l
                r

Store start and end times in two arrays. Walk through two pointers. Compare

Time    : O(n log n)
Space   : O(n)
"""


def min_meeting_rooms2(intervals):
    intervals.sort(key = lambda i: i.start)
    result = 0
    min_heap = []

    for interval in intervals:
        while len(min_heap) > 0 and interval.start >=  min_heap[0].end: # Remove all meetings that end before current meeting
            heappop(min_heap)

        heappush(min_heap, interval)
        result = max(result, len(min_heap))
        
    return result

"""
Approach 2:

Sort on start time. For each meeting, compare current meeting start time to heap end time

Time    : O(n log n)
Space   : O(n)
"""

intervals = []
intervals.append(interval.Interval(0, 30))
intervals.append(interval.Interval(30, 35))
intervals.append(interval.Interval(35, 40))
# intervals.append(interval.Interval(5, 8))
# intervals.append(interval.Interval(9, 15))

print(min_meeting_rooms2(intervals))