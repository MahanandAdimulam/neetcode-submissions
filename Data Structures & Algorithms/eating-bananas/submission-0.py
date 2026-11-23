import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        k = float('inf')
        while start<=end:
            mid = (start+end)//2
            total=0
            for pile in piles:
                rate = math.ceil(pile/mid)
                total+=rate
            if total<=h:
                k=min(k,mid)
                end=mid-1
            else:
                start=mid+1
        return k