class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        for key,value in d.items():
            if d[key]>=3:
                return False
        return True
        