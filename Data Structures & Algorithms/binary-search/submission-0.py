class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
            
        middle = len(nums)//2
        if (target == nums[middle]):
            return middle
        elif(target < nums[middle]):
            return self.search(nums[:middle], target)
        else:
            result = self.search(nums[middle+1:], target)
            if result == -1:
                return -1
            else:
                return middle + 1 + result