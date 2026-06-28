class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # create an array to store all areas
        # traverse the array and use two pointer method
        # length = min of two bars, width = diff between two bars
        # return the max value of the area array

        result = []

        left = 0
        right = len(heights) - 1
        for i in range(len(heights)):

            result.append(min(heights[left], heights[right]) * (right - left))

            if (heights[left]< heights[right]):
                left += 1
            else:
                right -= 1


        return max(result)