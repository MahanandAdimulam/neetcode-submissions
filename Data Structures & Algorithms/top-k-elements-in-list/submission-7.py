from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # print(count)
        r = []
        for k1, c in count.items():
            r.append([c, k1])
        r.sort(reverse=True)
        result = []
        # for i in range(k):
        #     result.append(r[i][1])
        for l in r[:k]:
            result.append(l[1])
            # k-=1
            # if k==0:
            #     break
        return result