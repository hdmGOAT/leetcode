class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        x1 = start
        x2 = start 
        while nums[x1] != target and nums[x2] != target:
            if x1 > 0:
                x1 -= 1
            if x2 < len(nums) -1:
                x2 += 1
        
        targ = x1 if nums[x1] == target else x2

        return abs(start-targ)

        
