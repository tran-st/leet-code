def combinationSum(candidates, target):
    result = []

    def dfs(i, current, total):
        # Two base cases
        if total == target:
            result.append(current.copy())
            return
        if i >= len(candidates) or total > target:
            return

        # Two decisions
        current.append(candidates[i])
        dfs(i, current, total + candidates[i])
        current.pop()
        dfs(i + 1, current, total)

    dfs(0, [], 0)

    
    return result

"""
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Approach:

Recursion. Subtract candidate from target, until < 0. Then try next candidate. If == 0,
return True

Time    : O()
"""

candidates = [2,3,6,7]
target = 7

print(combinationSum(candidates, target))