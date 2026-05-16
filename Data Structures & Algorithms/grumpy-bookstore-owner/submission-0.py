class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        nonGrumpy = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                nonGrumpy+=customers[i]
        

        l = 0
        r = minutes-1

        currGrumpy = 0
        maxGrumpy = -float('inf')

        for i in range(l,r+1):
            if grumpy[i] == 1:
                currGrumpy+=customers[i]
        
        while r < len(customers):

            maxGrumpy = max(maxGrumpy,currGrumpy)
            
            
            if grumpy[l] == 1:
                currGrumpy = currGrumpy - customers[l]
            l+=1
            
            r+=1
            if r < len(customers) and grumpy[r] == 1 :
                currGrumpy = currGrumpy + customers[r]
        


        
        return nonGrumpy+maxGrumpy
        
        