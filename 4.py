class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = nums1 + nums2
        result.sort()
        n = len(result)
        if n % 2 != 0:
            i = n//2
            return result[i]
        else:
            i = n//2
            return (result[i] + result[i-1])/2
        
