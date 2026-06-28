class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # O(1) space because we only edit the original list
        # O(n) time becuase list traversal
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] <= -1:
                return abs(nums[i])
            nums[abs(nums[i]) - 1] *= -1