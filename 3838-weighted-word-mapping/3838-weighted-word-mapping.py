class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        res=""
        for word in words:
            sum=0
            for i in range(len(word)):
                sum+=weights[(ord(word[i])-97)]
            ini=sum%26
            res+=chr(ord('z')-ini)
        return res

        