class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg=sum(nums)//len(nums)
        i=avg+1
        if avg<0:
            i=1
        while True:
            if i not in nums:
                return i
            else:
                i+=1
        


        