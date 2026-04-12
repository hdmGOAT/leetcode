from collections import defaultdict

class Solution(object):
    def minimumDistance(self, nums):
        m = defaultdict(list)
        for i, num in enumerate(nums):
            m[num].append(i)

        ans = float("inf")

        for idxs in m.values():
            if len(idxs) < 3:
                continue

            for i in range(len(idxs) - 2):
                a, b, c = idxs[i], idxs[i+1], idxs[i+2]
                dist = (b - a) + (c - b) + (c - a)
                ans = min(ans, dist)

        return ans if ans != float("inf") else -1
