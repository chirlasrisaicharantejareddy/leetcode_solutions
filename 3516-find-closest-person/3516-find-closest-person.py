class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        res1=abs(z-x)
        res2=abs(z-y)
        if res1==res2:
            return 0
        elif res1<res2:
            return 1
        else:
            return 2
        