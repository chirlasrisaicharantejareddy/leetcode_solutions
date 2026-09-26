class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        c=0
        for word in words1:
            if words2.count(word)==1 and words1.count(word)==1:
                c+=1
        return c
        