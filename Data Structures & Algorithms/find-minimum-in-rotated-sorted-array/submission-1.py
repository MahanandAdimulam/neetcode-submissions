class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        min_n = float('inf')
        while start<=end:
            mid = (start+end)//2
            min_n = min(min_n,nums[mid])
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return min_n      