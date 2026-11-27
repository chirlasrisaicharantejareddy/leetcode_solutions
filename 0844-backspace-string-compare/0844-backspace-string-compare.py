class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        top1=-1
        stack2=[]
        top2=-1
        for i in range(len(s)):
            if s[i].isalpha():
                stack1.append(s[i])
                top1+=1
            else:
                if top1!=-1:
                    stack1.pop()
                    top1-=1

        for i in range(len(t)):
            if t[i].isalpha():
                stack2.append(t[i])
                top2+=1
            else:
                if top2!=-1:
                    stack2.pop()
                    top2-=1
        res1="".join(stack1)
        res2="".join(stack2)
        return res1==res2
        
        
        