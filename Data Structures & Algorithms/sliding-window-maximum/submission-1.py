from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        candidate = deque()
        res = []
        for r in range(len(nums)):
            while candidate and nums[candidate[-1]] < nums[r]:
                candidate.pop()
            candidate.append(r)
            if candidate[0] < r-k+1:
                candidate.popleft()
            if r>=k-1:
                res.append(nums[candidate[0]])
        return res