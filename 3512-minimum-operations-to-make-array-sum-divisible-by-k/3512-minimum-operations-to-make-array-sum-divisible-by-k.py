class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res=sum(nums)%k
        return res
        