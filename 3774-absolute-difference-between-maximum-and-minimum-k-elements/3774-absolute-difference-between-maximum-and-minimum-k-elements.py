class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        small=0
        large=0
        for i in range(k):
            small+=nums[i]
        nums.reverse()
        for i in range(k):
            large+=nums[i]
        return abs(small-large)
        