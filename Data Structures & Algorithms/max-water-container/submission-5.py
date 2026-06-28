class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights = sorted(heights, reverse=True)
        # return heights[1]*heights[1]
        max = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if max < (j - i) * min(heights[i], heights[j]):
                    max = (j - i) * min(heights[i], heights[j])
                j += 1
        return max