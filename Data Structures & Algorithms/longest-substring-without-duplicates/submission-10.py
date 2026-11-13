class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}                       # char -> last index where we saw it
        l = 0
        longest = 0
        for r, ch in enumerate(s):
            if ch in last:
                l = max(l, last[ch] + 1)   # l only moves forward
            last[ch] = r
            longest = max(longest, r - l + 1)
        return longest