class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        d={}
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                d[arr[i]]+=1
        L=[]
        for key,value in d.items():
            if d[key]==1:
                L.append(key)
        if len(L)<k:
            return ""
        else:
            return L[k-1]
        