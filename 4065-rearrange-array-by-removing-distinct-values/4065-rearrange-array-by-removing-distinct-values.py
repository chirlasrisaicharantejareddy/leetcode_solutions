class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans=[]
        while len(nums)!=0:
            s=set(nums)
            L=list(s)
            L.sort()
            ans.extend(L)
            for i in s:
                nums.remove(i)
        return ans
        