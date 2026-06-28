class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def helper(start, end):

            if start > end:
                return -1

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[end]:
                if target > nums[mid] and target <= nums[end]:
                    return helper(mid+1, end)
                else:
                    return helper(start, mid-1)
            else:
                if target >= nums[start] and target < nums[mid]:
                    return helper(start, mid-1)
                else:
                    return helper(mid+1, end)



        return helper(0, len(nums)-1)