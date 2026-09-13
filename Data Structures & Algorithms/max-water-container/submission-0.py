class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area=0
        l=0
        r=len(heights)-1
        while l<r:
            width=r-l
            height=min(heights[l],heights[r])
            product=width*height
            if height==heights[l]:
                l+=1
            else:
                r-=1
            if product>area:
                area=product

        return area