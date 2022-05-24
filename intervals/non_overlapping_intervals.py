import interval


def eraseOverlapIntervals(intervals):
    if not intervals or len(intervals) == 0:
        return 0

    result = 0
    previous_end_time = intervals[0].end
    

    for start, end in intervals[1:]:
        if start >= previous_end_time: # No conflict
            previous_end_time = end
        else: # Clash
            result += 1
            previous_end_time = min(previous_end_time, end)

    return result

"""
[[1,2],[1,3],[2,3],[3,4]]
                     i

previous_end_time = 2
"""

"""
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Approach:

Go through each possible overlap. Track count

Time    : O(n^2)
Space   : O(1)

Approach 2:

[[1,2],[1,3],[2,3],[3,4]]

Sort on start time. Compare start time with end times. If overlap, delete longer end time. Track count

Time    : O(n log n)
Space   : O(1)
"""

intervals = []
intervals.append(interval.Interval(0, 30))
intervals.append(interval.Interval(30, 35))
intervals.append(interval.Interval(35, 40))
# intervals.append(interval.Interval(5, 8))
# intervals.append(interval.Interval(9, 15))

print(eraseOverlapIntervals(intervals))