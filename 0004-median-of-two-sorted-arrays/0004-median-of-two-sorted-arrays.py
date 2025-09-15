class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=nums1+nums2
        merged.sort()
        n=len(merged)
        if(n%2==0):
            return (merged[(n//2)-1]+merged[(n//2)])/2
        else:
            return merged[(n//2)]
        