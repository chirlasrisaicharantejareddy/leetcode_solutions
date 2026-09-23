class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-2):
            L=nums[i:i+3]
            print(L)
            if L[0]+L[-1]==L[1]/2:
                count+=1
        return count
        
        