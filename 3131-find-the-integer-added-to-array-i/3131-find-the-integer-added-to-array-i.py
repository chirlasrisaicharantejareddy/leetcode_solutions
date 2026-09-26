class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        if sum(nums1)==sum(nums2):
            return 0
        if sum(nums1)<sum(nums2):
            return (sum(nums2)-sum(nums1))//len(nums2)
        
        if sum(nums1)>sum(nums2):
            return (sum(nums2)-sum(nums1))//len(nums1)
        
        
        