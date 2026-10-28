from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        m = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1   # 'a' -> 0, 'b' -> 1, ...
            m[tuple(count)].append(s)            # list -> tuple so it can be a key
        return list(m.values())