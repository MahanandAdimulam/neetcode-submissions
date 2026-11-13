class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0]*len(height)
        maxR = [0]*len(height)
        max_l = 0
        max_r = 0
        total = 0
        for i in range(len(height)):
            max_l=max(max_l,height[i])
            maxL[i]=max_l
        for i in range(len(height)-1,-1,-1):
            max_r=max(max_r,height[i])
            maxR[i]=max_r
        for i in range(len(height)):
            sum = min(maxL[i],maxR[i])-height[i]
            if sum < 0:
                sum = 0
            total += sum
        return total