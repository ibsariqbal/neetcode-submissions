class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        curr_sum = 0
        for num in nums:
            
            if curr_sum < 0:
                curr_sum =0
            curr_sum +=num
            maxsum = max(maxsum,curr_sum)

        return maxsum
        