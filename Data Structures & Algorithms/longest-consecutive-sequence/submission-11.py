class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for i in numSet:
            if i-1 not in numSet:
                l=1
                while i+1 in numSet:
                    l+=1
                    i+=1
                longest=max(l,longest)
        return longest