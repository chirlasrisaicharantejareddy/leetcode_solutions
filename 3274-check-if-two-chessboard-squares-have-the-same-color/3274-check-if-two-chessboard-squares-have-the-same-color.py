class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        res1=0
        res2=0
        d={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
        res1=d[coordinate1[0]]+int(coordinate1[1])
        res2=d[coordinate2[0]]+int(coordinate2[1])
        if res1%2==0 and res2%2==0:
            return True
        if res1%2!=0 and res2%2!=0:
            return True
        return False
        

        