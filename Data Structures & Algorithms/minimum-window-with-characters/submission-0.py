from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        t_count=Counter(t)
        count = {}
        i=0
        need = len(t_count)
        have = 0
        res = ''
        best_l = float("inf")
        best =0
        for j in range(len(s)):
            count[s[j]] = count.get(s[j],0) + 1
            if count[s[j]] == t_count[s[j]]:
                have+=1
            while need==have:
                if j-i+1 < best_l:
                    best_l=j-i+1
                    best=i
                count[s[i]]-=1
                if count[s[i]] < t_count[s[i]]:
                    have-=1
                i+=1
        return "" if best_l == float("inf") else s[best:best + best_l]