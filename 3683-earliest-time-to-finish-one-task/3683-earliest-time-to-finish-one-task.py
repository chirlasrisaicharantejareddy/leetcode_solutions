class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        L=[]
        for task in tasks:
            L.append(sum(task))
        return min(L)

        