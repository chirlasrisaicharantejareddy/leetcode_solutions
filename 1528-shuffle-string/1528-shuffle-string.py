class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        res=""
        for i in range(max(indices)+1):
            INDEX=indices.index(i)
            res+=s[INDEX]
        return res

        