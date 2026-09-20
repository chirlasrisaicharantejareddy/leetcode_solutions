class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-1):
            res=sum(nums[i+1:])/len(nums[i+1:])
            if nums[i]>res:
                count+=1
        return count

        