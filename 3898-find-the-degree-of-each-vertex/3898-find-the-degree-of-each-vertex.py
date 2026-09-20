class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        L=[]
        for mat in matrix:
            res=mat.count(1)
            L.append(res)
        return L

        