class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        SUM=0
        temp=x
        while temp>0:
            rem=temp%10
            SUM+=rem
            temp=temp//10
        if x%SUM==0:
            return SUM
        else:
            return -1
        