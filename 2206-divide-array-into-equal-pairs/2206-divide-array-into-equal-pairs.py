class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        if len(nums)%2!=0:
            return False
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        for key,value in d.items():
            if d[key]%2!=0:
                return False
        return True
        