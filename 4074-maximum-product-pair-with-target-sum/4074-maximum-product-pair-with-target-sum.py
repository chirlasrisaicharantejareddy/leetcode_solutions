class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        finalresult=[]
        result=[]
        maximum_product=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target and nums[i]!=nums[j]:
                    if nums[i]>nums[j]:
                        finalresult.append([i,j])
                        result.append(nums[i]*nums[j])
                    else:
                        finalresult.append([j,i])
                        result.append(nums[i]*nums[j])
        print(finalresult)
        if len(finalresult)==0:
            return [-1,-1]
        
        return finalresult[result.index(max(result))]

                    
    


                        
        


        