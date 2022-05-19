def insert(intervals, newInterval):
    result = []

    if not intervals or len(intervals) == 0:
        return result

    for start, end in intervals:
        if newInterval[1] < start: # Before current interval, no clash
            result.append(newInterval)
        elif newInterval[0] > end: # After current interval, no clash
            result.append([start, end])
        else: # Clash. Merge
            start = min(start, newInterval[0])
            end = max(end, intervals[1])

            newInterval = [[start, end]]
            
    result.append(newInterval)

    return result
        

"""
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Approach:

[[4,5],[6,9],[12,13]]
 [3,4]

 result = [[1,3]]

 Iterate intervals from 0. If interval doesn't clash, insert

 Time   : O(n log n)
 Space  : O(n)
"""