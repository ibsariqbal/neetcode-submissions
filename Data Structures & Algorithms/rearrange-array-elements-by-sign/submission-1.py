class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        positive = []
        negative =[]
        
        for i in range(len(nums)):
            if nums[i]>0:
                positive.append(nums[i])
            if nums[i]<0:
                negative.append(nums[i])
        
        for i in range(len(nums)//2):
            res.append(positive[i])
            res.append(negative[i])
            

                
            

        return res

        