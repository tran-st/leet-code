def firstBadVersion(n):
    # 1.  Standard binary search left and right pointers
    # 2.  Mid pointer
    # 3.  If arr[mid] is bad and arr[mid - 1], we found it
    # 4.  Else, search the left side of the array

    left = 0
    right = n

    while left <= right:
        mid = left + (right - left) // 2

        if mid == 0:
            return mid + 1
        elif isBadVersion(mid) is True and isBadVersion(mid - 1) is False:
            return mid
        elif isBadVersion(mid) is False:
            left = mid + 1
        else:
            right = mid - 1

    return -1

"""
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Approach:

We can use binary search since the versions are sorted.
Instead of checking which numbers are greater than another, we 
would have to find where arr[mid - 1] is a good version and where
arr[mid] is the bad version

Time  : O(log n)
Space : O(1)

1 2 3 4 5 6 7 8 9 10
        ib(4) = true

        ib(5) = true
        ib(3) = false
        if(4) = true

        
"""