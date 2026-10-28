class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i, n in enumerate(nums):
            m[n] = i
        for i, n in enumerate(nums):
            v = target - n
            if v in m and m[v]!=i:
                return [i,m[v]]
        return []
#Best