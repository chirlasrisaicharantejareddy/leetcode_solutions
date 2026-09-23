class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        for i in range(1,len(nums)):
            sum1=sum(nums[0:i])
            sum2=sum(nums[i:])
            if abs(sum1-sum2)%2==0:
                count+=1
        return count
        