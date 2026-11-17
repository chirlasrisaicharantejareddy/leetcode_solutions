class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        L=[0]*26
        M=[0]*26
        for i in range(len(s)):
            L[ord(s[i])-97]+=1
        for i in range(len(t)):
            M[ord(t[i])-97]+=1
        print(L)
        print(M)
        for i in range(26):
            if L[i]!=M[i]:
                return chr(97+i)
        
        
        
        