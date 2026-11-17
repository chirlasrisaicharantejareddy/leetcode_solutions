class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        L=[]
        for i in range(1,len(nums)):
            flag=1
            for j in range(0,i):
                if nums[i]<nums[j]:
                    flag=0
                    break
            if flag==1:
                L.append(nums[i])
        if len(nums)==1 or len(L)==0:
            return 0
        return nums.index(L[-1])
