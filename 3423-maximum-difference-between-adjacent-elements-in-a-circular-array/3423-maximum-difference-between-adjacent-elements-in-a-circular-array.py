class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        MAX=-1
        for i in range(len(nums)-1):
            if MAX<abs(nums[i]-nums[i+1]):
                MAX=abs(nums[i]-nums[i+1])
        return max(MAX,abs(nums[-1]-nums[0]))


        