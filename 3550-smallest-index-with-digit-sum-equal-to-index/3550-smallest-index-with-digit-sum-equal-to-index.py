class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum=0
            temp=nums[i]
            while temp>0:
                rem=temp%10
                sum+=rem
                temp=temp//10
            if sum==i:
                return i
        return -1
        