class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp=n
        rev=0
        while temp>0:
            rem=temp%10
            rev=(rev*10)+rem
            temp=temp//10
        return abs(n-rev)
        