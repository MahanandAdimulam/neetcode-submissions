class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_num = sorted(nums)
        for i in range(1,len(nums)):
            if sorted_num[i] == sorted_num[i-1]:
                return True
        return False
        