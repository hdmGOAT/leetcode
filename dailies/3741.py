from collections import defaultdict


class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = defaultdict(list)
        for i, num in enumerate(nums):
            count[num].append(i)
        
        minimum = float('inf')
        for l in count.values():
            for idx in range(len(l) - 2):
                i, j, k = l[idx], l[idx+1], l[idx+2]
                dist = 2 * (k - i)
                minimum = min(minimum, dist)
        
        return -1 if minimum == float('inf') else minimum
