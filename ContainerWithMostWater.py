class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        i=0
        j=len(height)-1
        while(i<j):
            if(height[i]<height[j]):
                area=(height[i]*(j-i))
                maxWater=max(maxWater,area)
                i+=1
            else:
                area=(height[j]*(j-i))
                maxWater=max(maxWater,area)
                j-=1
            
        return maxWater