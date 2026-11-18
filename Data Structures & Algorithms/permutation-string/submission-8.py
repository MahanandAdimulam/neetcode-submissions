from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2Count = Counter(s1)
        need = len(s2Count)
        for i in range(len(s2)):
            count, cur = {}, 0
            for j in range(i, len(s2)):
                count[s2[j]] = 1 + count.get(s2[j],0)
                if s2Count.get(s2[j],0) < count[s2[j]]:
                    break
                if s2Count.get(s2[j],0) == count[s2[j]]:
                    cur+=1
                if cur == need:
                    return True
        return False