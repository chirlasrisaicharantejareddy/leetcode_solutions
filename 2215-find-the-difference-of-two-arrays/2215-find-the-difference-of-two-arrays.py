class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        res=[]
        s=set(nums1)
        s=list(s)
        L1=[]
        L2=[]
        for i in range(len(s)):
            if s[i] not in nums2:
                L1.append(s[i])
        p=set(nums2)
        p=list(nums2)
        for i in range(len(p)):
            if p[i] not in nums1:
                L2.append(p[i])
        res.append(list(set(L1)))
        res.append(list(set(L2)))
        return res
        