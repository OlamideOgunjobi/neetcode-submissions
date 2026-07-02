class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        left, right = 1, max(piles)
        result = right

        while left <= right:
            
            mid = (left + right) // 2
            hours = 0
            for val in piles:
                hours += math.ceil(val / mid)

            if hours <= h:
                if mid < result:
                    result = mid
                right = mid-1
            else:
                left = mid+1

        return result