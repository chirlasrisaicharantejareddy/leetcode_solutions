class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        x=10
        flag=0
        while True:
            if n-x>=0:
                n=n-x
            else:
                break
            x-=1
            flag+=1
        if flag%2!=0:
            return True
        else:
            return False
        



        