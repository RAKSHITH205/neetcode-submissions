class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        max_area=0
        for i in range(n):
            for j in range(i+1,n):
                curr_area=(j-i)*min(heights[i],heights[j])
                max_area=max(max_area,curr_area)
        return max_area
                
        