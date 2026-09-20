class Solution:
    def reverseDegree(self, s: str) -> int:
        product=1
        f="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(s)):
            product+=((i+1)*(26-f.index(s[i])))
        return product-1
