class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        L=[]
        for key,value in d.items():
            if d[key]==2:
                L.append(key)
        return L

        