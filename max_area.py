class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxArea = 0
        
        while start != end:
            area = min(height[start], height[end]) * (end - start)
            if area > maxArea:
                maxArea = area
            
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            
        
        return maxArea