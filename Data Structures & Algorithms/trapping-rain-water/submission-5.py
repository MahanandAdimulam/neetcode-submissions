class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        maxL=height[l]
        maxR=height[r]
        total=0
        while l<r:
            if height[l]<height[r]:
                sum=min(maxL,maxR)-height[l]
                if sum<0:
                    sum=0
                total+=sum
                l+=1
                maxL=max(maxL,height[l])
            else:
                sum=min(maxL,maxR)-height[r]
                if sum<0:
                    sum=0
                total+=sum
                r-=1
                maxR=max(maxR,height[r])            
        return total
#Two Pointers