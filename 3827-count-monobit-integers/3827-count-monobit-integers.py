class Solution:
    def countMonobit(self, n: int) -> int:
        count=0
        for i in range(0,n+1):
            if i==0 or i==1:
                count+=1
            else:
                binary=bin(i)[2:]
                print(binary)
                print(binary.count("0"))
                print(binary.count("1"))
                if len(binary)==binary.count("0") or len(binary)==binary.count("1"):
                    count+=1
        return count
        