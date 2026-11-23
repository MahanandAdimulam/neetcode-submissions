class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)

        while start <= end:
            mid = (start + end) // 2

            # hours needed at speed mid, rounding each pile up
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid
                if hours > h:
                    break

            if hours <= h:
                end = mid - 1
            else:
                start = mid + 1

        return start