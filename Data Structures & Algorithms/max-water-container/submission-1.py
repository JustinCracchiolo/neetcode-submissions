class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # the height is the min height of both pillars 
        # the width is the subtraction of the indexes. You want to maximize
        # since we want to max area, start and the front and end with two pointers 
        # move the one with the min height

        l, r = 0, len(heights) - 1 
        h, w = 0, 0
        max_area = 0

        while l < r:
            h = min(heights[l], heights[r])
            w = r - l 
            max_area = max(h*w, max_area)

            if heights[l] < heights[r]:
                l += 1 
            else:
                r -= 1 
        
        return max_area

