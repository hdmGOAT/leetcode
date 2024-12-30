'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p = 0
        lastel = m-1
        if n == 0: return

        for i in range(m+n):
            if p >= n:
                break
            if nums2[p] < nums1[i] or (i >= lastel and nums1[i] == 0):
                nums1.insert(i, nums2[p])
                nums1.pop()
                p += 1
                lastel += 1
                