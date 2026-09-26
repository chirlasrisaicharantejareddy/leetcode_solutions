class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum1=0
        sum2=0
        for i in range(len(nums)):
            if len(str(nums[i]))==2:
                sum1+=nums[i]
            else:
                sum2+=nums[i]
        if sum1==sum2:
            return False
        else:
            return True
        