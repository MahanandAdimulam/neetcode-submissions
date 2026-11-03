from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # arr = [[]]*(len(nums)+1)
        arr =[]
        for _ in range(len(nums)+1):
            arr.append([])
        count = Counter(nums)
        r=[]
        for n,c in count.items():
            arr[c].append(n)
        for v in arr[::-1]:
            if v!=[]:
                r.extend(v)
            if len(r)==k:
                return r
            elif len(r)>k:
                return r[:k]        