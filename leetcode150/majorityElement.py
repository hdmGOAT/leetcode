'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 aa
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        appearances = {}

        for num in nums:
            if num not in appearances:
                appearances[num] = 1
            else:
                appearances[num] +=1

        max_key = max(appearances, key=appearances.get)
        return max_key


        