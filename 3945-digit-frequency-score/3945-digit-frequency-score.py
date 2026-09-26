class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d={}
        n=str(n)
        for i in range(len(n)):
            if n[i] not in d:
                d[n[i]]=1
            else:
                d[n[i]]+=1
        sum=0
        print(d)
        for key,value in d.items():
            mul=int(key)*value           
            sum=sum+mul
        return sum
        