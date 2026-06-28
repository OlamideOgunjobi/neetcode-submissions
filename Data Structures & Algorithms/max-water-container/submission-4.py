class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights = sorted(heights, reverse=True)
        # return heights[1]*heights[1]
        max = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                left, right = i, j   # left and right
                if not(left < right):
                    break
                if max < (right - left) * min(heights[left], heights[right]):
                    max = (right - left) * min(heights[left], heights[right])
                right += 1
        return max