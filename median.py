class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # if length of nums1 + nums2 is divisible by 2 then we retrieve the average of the two middle list
        # To get the two middle list we divide mid_1 = l/2 and mid_2 = mid_1-1 
        # else we get the middle element by mid = l/2
        s = sorted(nums1+nums2)
        l = len(s)

        if l%2 == 0:
            mid_1 = s[l//2]
            mid_2 = s[(l//2)-1]
            return (mid_1+mid_2)/2

        else:
            return s[l//2]