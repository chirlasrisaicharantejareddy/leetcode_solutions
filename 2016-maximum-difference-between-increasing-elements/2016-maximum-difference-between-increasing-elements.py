class Solution:
    def maximumDifference(self, nums: list[int]) -> int:

        max=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    if abs(nums[j]-nums[i])>max:
                        max=nums[j]-nums[i]
        return max
        