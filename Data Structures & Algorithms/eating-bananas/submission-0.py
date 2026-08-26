class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        answer=r
        while l<=r:
            m=(l+r)//2
            hrs=0
            for p in piles:

                hrs+=(p+m-1)//m
            if hrs<=h:
                answer=m
                r=m-1
            else:
                l=m+1
        return answer

        