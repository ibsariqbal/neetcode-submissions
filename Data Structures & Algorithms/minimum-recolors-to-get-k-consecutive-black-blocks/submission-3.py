class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        countB = 0
        L = 0
        res = k

        for R in range(len(blocks)):
            if blocks[R] == 'B':
                countB+=1

            if R - L + 1 > k :
                if blocks[L] == 'B':
                    countB-=1
                L+=1
            if R - L + 1 == k:
                res = min(res,k-countB)

        
        return res

        