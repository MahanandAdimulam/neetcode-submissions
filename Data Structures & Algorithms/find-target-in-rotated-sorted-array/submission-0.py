class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            # left half is sorted
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1      # target is inside the sorted left half
                else:
                    start = mid + 1
            # otherwise the right half is sorted
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1    # target is inside the sorted right half
                else:
                    end = mid - 1

        return -1