import interval


def canAttendMeetings(intervals):
    if not intervals or len(intervals) == 1:
        return True

    intervals.sort(key = lambda i : i.start)

    for i in range(1, len(intervals)):
        left = intervals[i - 1]
        right = intervals[i]

        if right.start < left.end:
            return False

    return True

"""
[(0,30),(29,30),(15,20)]
  l
         r

"""

"""
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict

Approach:

Check each and every meeting if they clash

Time    : O(n^2)
Space   : O(1)


Approach 2:

[(0,30),(5,10),(15,20)]
max_start = 5
min_end = 10

Sort by start time. If meeting starts after and ends before, they clash

Time    : O(n log n)
Space   : O(1)
"""

intervals = []
# intervals.append(interval.Interval(0, 30))
# intervals.append(interval.Interval(5, 10))
# intervals.append(interval.Interval(15, 20))
intervals.append(interval.Interval(5, 8))
intervals.append(interval.Interval(9, 15))

# intervals = [(0,30),(5,10),(15,20)]

print(canAttendMeetings(intervals))