class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        L=[]
        while len(nums)!=0:
            num1=min(nums)
            nums.remove(num1)
            num2=min(nums)
            nums.remove(num2)
            L.append(num2)
            L.append(num1)
        return L
        