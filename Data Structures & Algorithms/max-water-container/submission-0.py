class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea=0

        left,right=0,len(heights)-1
        mini=0

        while left < right:
            mini=min(heights[left], heights[right])
            # print(f"mini: {mini}")
            width=right - left
            # print(f"width:{width}")
            area=mini*width
            maxarea=max(maxarea,area)
            # print(f"maxarea: {maxarea}")

            if heights[left] < heights[right]:
                left+=1

            else:
                right-=1

        return maxarea