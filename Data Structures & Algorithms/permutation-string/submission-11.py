from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        s1Count=Counter(s1)
        need = len(s1Count)
        for i in range(len(s2)):
            count={}
            have = 0
            for j in range(i,len(s2)):
                ch = s2[j]
                count[ch] = count.get(ch,0) + 1
                if s1Count.get(ch,0)<count[ch]:
                    break
                elif s1Count.get(ch,0) == count[ch]:
                    have+=1
                if have==need:
                    return True
        return False