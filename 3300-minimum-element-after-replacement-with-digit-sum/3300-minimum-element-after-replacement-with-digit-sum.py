class Solution:
    def minElement(self, nums: List[int]) -> int:
        L=[]
        for i in range(len(nums)):
            SUM=0
            temp=nums[i]
            while temp>0:
                rem=temp%10
                SUM+=rem
                temp=temp//10
            L.append(SUM)
        return min(L)

        