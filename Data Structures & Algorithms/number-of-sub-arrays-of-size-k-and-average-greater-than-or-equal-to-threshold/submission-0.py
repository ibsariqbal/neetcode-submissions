class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        window = sum(arr[:k])
        res = 0
        l = 0
        r = k-1

        while r < len(arr):
            if window//k >= threshold :
                res+=1
            window = window - arr[l]
            l+=1
            r+=1
            if r < len(arr):
                window = window + arr[r]
        
        return res
        