''' Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        
        """
        
        if k < 1:
            return
        l = len(nums)
        
        while k > l:
            k -= l

        n = abs(l - k)

        
        a = nums[n:]
        b = nums[:n]


        nums[:] = a + b

        
        