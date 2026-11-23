class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                # drop is to the right of mid, so min is in the right half
                start = mid + 1
            else:
                # right half is sorted, so min is at mid or to its left
                end = mid

        return nums[start]