class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        X=0
        for operation in operations:
            if operation=="++X" or operation=="X++":
                X+=1
            else:
                X-=1
        return X
        