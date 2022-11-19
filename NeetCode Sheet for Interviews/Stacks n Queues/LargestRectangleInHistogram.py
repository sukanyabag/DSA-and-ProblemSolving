'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair = (idx, height)

        for i, h in enumerate(heights):
            startidx = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                startidx = idx
            stack.append((startidx, h))

        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
