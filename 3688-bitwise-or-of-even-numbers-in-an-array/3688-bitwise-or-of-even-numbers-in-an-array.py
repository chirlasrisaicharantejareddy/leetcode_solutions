class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        sum=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                sum=(sum|nums[i])
        return sum