class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # array is sorted in ascending order
        # use two pointer method to find the sum
        # if the sum == target, return the index (add one to the indecies since return value should be 1-indexed)
        # if the sum < target, move left
        # if the sum > target, move right
        
        left = 0
        right = len(numbers) - 1


        while left < right:
            
            val = numbers[left] + numbers[right]
            if val == target:
                return [left+1, right+1]
            elif val < target:
                left += 1
            elif val > target:
                right -= 1