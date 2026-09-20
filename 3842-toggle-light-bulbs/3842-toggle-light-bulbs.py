class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        d={}
        L=[]
        nums=bulbs
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            elif nums[i] in d:
                if d[nums[i]]==1:
                    d[nums[i]]=0
                else:
                    d[nums[i]]=1
        for key,value in d.items():
            if d[key]==1:
                L.append(key)
        L.sort()
        return L
        