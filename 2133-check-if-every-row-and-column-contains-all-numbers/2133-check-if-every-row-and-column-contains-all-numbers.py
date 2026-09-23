class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        L=[]
        for i in range(1,len(matrix)+1):
            L.append(i)
        for i in range(len(matrix)):
            res=[]
            for j in range(len(matrix[0])):
                if matrix[i][j] not in res:
                    res.append(matrix[i][j])
            if len(res)!=len(L):
                return False
        for i in range(len(matrix)):
            res=[]
            for j in range(len(matrix)):
                if matrix[j][i] not in res:
                    res.append(matrix[j][i])
            if len(res)!=len(L):
                return False
        return True

