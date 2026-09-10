class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)
        k=0
        sum_b=0

        while low<=high:
            mid=low+(high-low)//2
            sum_b=sum(-(p//-mid) for p in piles)
            
            if sum_b<=h:
                k=mid
                high=mid-1
            else:
                low=mid+1

        return k