class Solution:
    def findMedianSortedArrays(nums1, nums2):
        l1 = nums1 + nums2
        l1.sort()
        sum = 0
        for i in range(0, len(l1)):
            sum = sum + l1[i]

        if len(l1) == 1:
            output = l1[0]
        elif len(l1) == 2:
            median1 = l1[1]
            median2 = l1[0]
            output = (median1 + median2) / 2
        else:
            if int(len(l1)) % 2 != 0:
                output = l1[int(len(l1) / 2)]
            else:
                median1 = l1[int(len(l1) / 2) - 1]
                median2 = l1[int(len(l1) / 2)]
                output = (median1 + median2) / 2

        return output

    print(findMedianSortedArrays([], [1, 2, 3, 4, 5, 6]))
