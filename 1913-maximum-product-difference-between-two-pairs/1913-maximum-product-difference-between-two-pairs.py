class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
       res1=max(nums)
       nums.remove(res1)
       res2=max(nums)
       nums.remove(res2)
       res3=min(nums)
       nums.remove(res3)
       res4=min(nums)
       nums.remove(res4)
       return (res1*res2)-(res3*res4)