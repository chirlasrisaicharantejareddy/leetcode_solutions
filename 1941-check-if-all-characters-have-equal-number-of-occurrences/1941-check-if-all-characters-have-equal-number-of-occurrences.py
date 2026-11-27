class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
        L=[]
        print(d)
        for value in d.values():
            L.append(value)
        for i in range(len(L)-1):
            if L[i]!=L[i+1]:
                return False
        return True
        