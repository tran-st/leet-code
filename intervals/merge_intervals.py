def merge(intervals):
    result = []

    if not intervals or len(intervals) == 0:
        return result

    intervals.sort()
    result.append[intervals[0]]

    for start, end in intervals[1:]:
        last_end_time = result[-1][1]

        if start <= last_end_time:
            result[-1][1] = max(last_end_time, end)
        else:
            result.append((start, end))

    return result

"""
[[1,3],[2,6],[8,10],[15,18]]

last_end_time = 3
start = 2
last_end_time = max(last_end_time, end)
"""

"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Approach:

[[1,3],[2,6],[3,9],[15,18]]
  l
       r

Sort by start time. Two pointers. If overlap, take max of end time. Push to result

Time    : O(n log n)
Space   : O(n)
"""