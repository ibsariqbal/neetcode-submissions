class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n

        p,n=0,1

        for i in range(len(nums)):
            if (nums[i]>0):
                res[p]= nums[i]
                p+=2
            else:
                res[n]= nums[i]
                n+=2

        return res
