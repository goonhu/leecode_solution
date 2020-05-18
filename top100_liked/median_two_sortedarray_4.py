

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        list_total = nums1 + nums2
        list_total.sort()

        if len(list_total) % 2 != 0:
            return float(list_total[len(list_total )//2])
        else:
            return (list_total[len(list_total )//2] + list_total[len(list_total )//2 - 1])/2


