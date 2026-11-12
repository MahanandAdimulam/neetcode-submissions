class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums.sort()
        longest = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue                  # duplicate: skip
            elif nums[i] == nums[i - 1] + 1:
                cur += 1                  # run continues
            else:
                cur = 1                   # gap: start a new run
            longest = max(longest, cur)   # keep the best so far
        return longest