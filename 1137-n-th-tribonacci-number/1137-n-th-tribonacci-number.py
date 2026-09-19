class Solution:
    def tribonacci(self, n: int) -> int:
        L=[]
        L.append(0)
        L.append(1)
        L.append(1)
        for i in range(3,n+1):
            L.append(L[i-1]+L[i-2]+L[i-3])
        print(L)
        return L[n]
        