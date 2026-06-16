class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        positive = []
        negative =[]
        
        for i in range(len(nums)):
            if nums[i]>0:
                positive+=[nums[i]]
            if nums[i]<0:
                negative+=[nums[i]]
        
        for i in range(len(nums)//2):
            res+=[positive[i],negative[i]]
            

                
            

        return res

        