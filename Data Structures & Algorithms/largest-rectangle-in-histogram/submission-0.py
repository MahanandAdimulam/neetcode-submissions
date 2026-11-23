class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []          # pairs of (start index, height)
        best = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                best = max(best, height * (i - idx))
                start = idx
            stack.append((start, h))
        for idx, height in stack:
            best = max(best, height * (len(heights) - idx))
        return best