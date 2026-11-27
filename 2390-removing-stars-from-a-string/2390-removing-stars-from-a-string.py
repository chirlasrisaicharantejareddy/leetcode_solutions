class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        top=-1
        for i in range(len(s)):
            if s[i].isalpha():
                top+=1
                stack.insert(top,s[i])
            else:
                stack.pop()
        res="".join(stack)
        return res

        