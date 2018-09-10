class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        i, j = 0, n-1
        result = (j-i)*min(height[i], height[j])
        while i<j:
            if height[i] < height[j]:
                i+=1
                result = max(result, (j-i)*min(height[i], height[j]))
            else:
                j-=1
                result = max(result, (j-i)*min(height[i], height[j]))
        return result
